##############################################################################
##############################################################################
# Imports and logging setup 
##############################################################################

import argparse
import collections 
import itertools 
import json 
import logging 
import time 

import numpy 
from sklearn.metrics import confusion_matrix
import issue_db_api


logger = logging.getLogger('Agreement Analyser')
handler = logging.StreamHandler()
formatter=  logging.Formatter(
    fmt='[{name}][{asctime}][{levelname}]: {msg}',
    style='{'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

##############################################################################
##############################################################################
# Analyser
##############################################################################


class AgreementAnalyser:

    def __init__(self):
        self._labels = {}
        self._annotations = {}
        self._authors = set()

    def add_document(self, identifier: str, label: issue_db_api.Label):
        self._annotations[identifier] = {}
        self._labels[identifier] = label 

    def add_entry(self, 
                  document: str, 
                  author: str, 
                  label: issue_db_api.Label):
        if document not in self._annotations:
            raise ValueError(f'Unregistered document: {document}')
        self._annotations[document][author] = label 
        self._authors.add(author)

    def serialize_dataset_composition(self):
        counter = collections.defaultdict(int)
        for label in self._labels.values():
            counter[label_to_string(label)] += 1
        return {
            lab: counter[lab]
            for lab in get_all_labels()
        }

    def serialize_agreement(self):
        matrices = []
        for a, b in itertools.combinations(self._authors, r=2):
            matrices.extend(self._compare_authors_binary(a, b))
        for a, b in itertools.combinations(self._authors, r=2):
            matrices.append(self._compare_authors_total(a, b))
        return [m.serialize() for m in matrices] 

    def _compare_authors_binary(self, author_a, author_b):
        common = [
            (labels[author_a], labels[author_b])
            for labels in self._annotations.values()
            if author_a in labels and author_b in labels 
        ]
        return [
            AgreementMatrix(
                title='existence',
                labels=['No', 'Yes'],
                row_label=author_a,
                col_label=author_b,
                matrix=confusion_matrix(
                    [pair[0].existence for pair in common],
                    [pair[1].existence for pair in common]
                )
            ),
            AgreementMatrix(
                title='executive',
                labels=['No', 'Yes'],
                row_label=author_a,
                col_label=author_b,
                matrix=confusion_matrix(
                    [pair[0].executive for pair in common],
                    [pair[1].executive for pair in common]
                )
            ),
            AgreementMatrix(
                title='property',
                labels=['No', 'Yes'],
                row_label=author_a,
                col_label=author_b,
                matrix=confusion_matrix(
                    [pair[0].property for pair in common],
                    [pair[1].property for pair in common]
                )
            )
        ]
    
    def _compare_authors_total(self, author_a, author_b):
        common = [
            (label_to_string(labels[author_a]), label_to_string(labels[author_b]))
            for labels in self._annotations.values()
            if author_a in labels and author_b in labels 
        ]
        categories = get_all_labels()
        return AgreementMatrix(
            title='total',
            labels=categories,
            row_label=author_a,
            col_label=author_b,
            matrix=confusion_matrix(
                [pair[0] for pair in common],
                [pair[1] for pair in common],
                labels=categories
            )
        )


##############################################################################
##############################################################################
# Matrix class 
##############################################################################


class AgreementMatrix:
    
    def __init__(self,
                 title,
                 labels,
                 row_label, 
                 col_label,
                 matrix: numpy.ndarray):
        self._title = title 
        self._labels = labels
        self._rows = row_label 
        self._cols = col_label
        self._matrix = matrix 

    def kappa(self):
        p_o = self.agreement()
        p_c = self.random_agreement()
        return (p_o - p_c) / (1 - p_c)

    def random_agreement(self):
        rows = self._matrix.sum(axis=1)
        cols = self._matrix.sum(axis=0)
        total = self._matrix.sum()
        return rows.dot(cols) / (total ** 2) 

    def agreement(self):
        return self._matrix.diagonal().sum() / self._matrix.sum()
    
    def serialize(self):
        return {
            'matrix': self._matrix.tolist(),
            'row_annotator': self._rows,
            'col_annotator': self._cols,
            'labels': self._labels,
            'agreement': self.agreement(),
            'total_issues': int(self._matrix.sum()),
            'kappa': self.kappa(),
            'title': self._title
        }  


##############################################################################
##############################################################################
# Helper functions 
##############################################################################


def maybe_extract_labelling_comment(text: str) -> issue_db_api.Label | None:
    original = text 
    text = text.lower()
    if text.startswith('label:'):
        text = text.removeprefix('label:')
        label = issue_db_api.Label(
            existence='existence' in text,
            executive='executive' in text,
            property='property' in text
        )
        if label.non_architectural:
            assert 'non-arch' in text or 'non-architectural' in text, original 
        return label 
    return None 


def label_to_string(label: issue_db_api.Label) -> str:
    parts = []
    if label.existence: parts.append('existence')
    if label.executive: parts.append('executive')
    if label.property: parts.append('property')
    if not parts:
        return 'non-architectural'
    return '/'.join(sorted(parts))


def get_all_labels():
    return sorted([
        label_to_string(issue_db_api.Label(existence=True, executive=True, property=True)),
        label_to_string(issue_db_api.Label(existence=True, executive=True, property=False)),
        label_to_string(issue_db_api.Label(existence=True, executive=False, property=True)),
        label_to_string(issue_db_api.Label(existence=True, executive=False, property=False)),
        label_to_string(issue_db_api.Label(existence=False, executive=True, property=True)),
        label_to_string(issue_db_api.Label(existence=False, executive=True, property=False)),
        label_to_string(issue_db_api.Label(existence=False, executive=False, property=True)),
        label_to_string(issue_db_api.Label(existence=False, executive=False, property=False)),
    ])


##############################################################################
##############################################################################
# Main Function
##############################################################################


def main(url: str,
         tags: list[str], 
         include_authors: list[str] | None, 
         exclude_authors: list[str] | None):
    logger.info(f'Database URL: {url}')
    repo = issue_db_api.IssueRepository(
        url, label_caching_policy='use_local_after_load'
    )
    
    query = issue_db_api.Query().land(
        issue_db_api.Query().tag('has-label'),
        issue_db_api.Query().lor(
            *(
            issue_db_api.Query().tag(tag) for tag in tags 
            )
        )
    )
    logger.info(f'Searching for issues with tags: {tags}')
    logger.debug(f'Query: {query.to_json()}')
    
    logger.info(f'Searching for issues...')
    start = time.time()
    issues = repo.search(query, load_labels=True)
    logger.info(
        f'Retrieved {len(issues)} issues. Took {time.time() - start:.3f} seconds'
    )

    analyser = AgreementAnalyser()

    logger.info('Extracting labelling comments from issues...')
    start = time.time()
    for issue in issues:
        analyser.add_document(issue.identifier, issue.manual_label)
        for comment in issue.labelling_comments:
            if exclude_authors is not None and comment.author in exclude_authors:
                continue 
            if include_authors is not None and comment.author not in include_authors:
                continue
            if (label := maybe_extract_labelling_comment(comment.body)) is not None:
                analyser.add_entry(issue.identifier, comment.author, label) 

    logger.info(
        f'Finished extracting comments. Took {time.time() - start:.3f} seconds'
    )

    logger.info('Computing dataset decomposition')
    serialized = analyser.serialize_dataset_composition()
    for key, amount in serialized.items():
        print(f'{key.ljust(30)} -- {amount}')
    
    logger.info('Saving results to `dataset.json`...')
    with open('dataset.json', 'w') as file:
        json.dump(serialized, file)

    logger.info('Computing confusion matrices')

    serialized = analyser.serialize_agreement()
    for matrix in serialized:
        title = matrix['title']
        author_a = matrix['row_annotator']
        author_b = matrix['col_annotator']
        kappa = matrix['kappa']
        print(f'{title.ljust(20)} - {author_a.ljust(20)} vs {author_b.ljust(20)} -- kappa: {kappa}')

    logger.info('Saving results to `agreement.json`...')
    with open('agreement.json', 'w') as file:
        json.dump(serialized, file, indent=2)

    logger.info('Done')
    


##############################################################################
##############################################################################
# Program entrypoints
##############################################################################



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        __name__, 'A utility tool to compute annotator agreement in Maestro.'
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--include-authors', 
                        nargs='+',
                        type=str, 
                        default=None,
                        help='Authors to include in the analysis. Mutually exclusive with --exclude-authors.')
    
    group.add_argument('--exclude-authors',
                        nargs='+',
                        type=str,
                        default=None,
                        help='Authors to exclude from the analysis. Mutually exlusive with --include-authors.')
    parser.add_argument('--tags',
                        nargs='+',
                        type=str,
                        required=True,
                        help='Tags used to retrieve the issues to analyse')
    parser.add_argument('--db-url', 
                        type=str,
                        required=True,
                        help='URL of the database to connect to.')
    args = parser.parse_args()
    main(
        url=args.db_url,
        tags=args.tags,
        include_authors=args.include_authors,
        exclude_authors=args.exclude_authors
    )

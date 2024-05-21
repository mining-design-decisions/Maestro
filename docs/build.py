"""
Utility script to help build Maestro's documentation.

Various parts of Maestro's documentation are automatically generated.
This script performs the required pre-flight checks and 
performs this generation.
"""

from __future__ import annotations 

import argparse 
import collections
import contextlib
import dataclasses
import logging 
import os 
import subprocess
import sys 
import typing 

import requests

##############################################################################
##############################################################################
# UML Builder
##############################################################################


def build_uml_files(java_path: str, plantuml_path: str):
    logger.info('Building UML files') 
    for root, _,  files in os.walk('.'):
        for file in files:
            if file.endswith('.pu'):
                
                build_uml(java_path, plantuml_path, root, file)


def build_uml(java_path: str, plantuml_path: str, root: str, filename: str):
    path = os.path.join(root, filename)
    logger.info(f'Creating image for file {path}')
    command = [
        java_path,
        '-jar',
        plantuml_path,
        '-tsvg',
        #'-o',
        #root,
        path 
    ]
    p = subprocess.run(command)
    p.check_returncode()


##############################################################################
##############################################################################
# Markdown Writers for DL Manager Documentation
##############################################################################


def join_items(x):
    if len(x) == 1:
        return x[0]
    *y, z = x 
    return ', '.join(y) + ' and ' + z 



class ArgumentCondition(typing.TypedDict):
    name: str
    value: typing.Any 


@dataclasses.dataclass
class EndpointArgument:
    name: str 
    description: str 
    nargs: str 
    arg_type: str
    required: bool 
    options: list[str] 
    has_default: bool 
    default: typing.Any | None 
    null_if: ArgumentCondition | None 
    null_unless: ArgumentCondition | None 

    def write_markdown(
        self, writer: MarkdownWriter, constraints, argument_lists, parent_name: str, dynamic_enums
    ):
        #writer.header(f'{self.name}', size=4)
        with writer.collapsible(self.name):
            writer.text_italic(self.description)
            match self.arg_type:
                case 'enum':
                    opts = ', '.join(f'`{y}`' for y in self.options)
                    writer.text(f'Argument type: enum (possible values: {opts})')
                case 'arglist':
                    writer.text(f'Argument type: [arglist](./dl_manager_arglist__{parent_name}__{self.name}.md)')
                case 'hyper_arglist':
                    writer.text(f'Argument type: [hyper_arglist](./dl_manager_arglist__{parent_name}__{self.name}.md)')
                case 'dynamic_enum':
                    opts = ', '.join(f'`{y}`' for y in dynamic_enums[parent_name][self.name])
                    writer.text(f'Argument type: enum (possible values: {opts})')
                case _ as x:
                    writer.text(f'Argument type: {x}')
            match self.nargs:
                case '*':
                    writer.text('Numer of arguments: A list of zero or more values.')
                case '+':
                    writer.text('Numer of arguments: A list of one or more values.')
                case '1':
                    writer.text('Numer of arguments: A single value.')
                case _ as x:
                    writer.text(f'Numer of arguments: {x}.')
            if self.required:
                writer.text('This argument is mandatory and must be given.')
            else:
                writer.text('This argument is optional')
            if self.null_if is not None:
                writer.text(
                    f'This argument should be `null` if `{self.null_if["name"]}` '
                    f'is equal to `{self.null_if["value"]}`'
                )
            if self.null_unless is not None:
                writer.text(
                    f'This argument should be `null` unless `{self.null_unless["name"]}` '
                    f'is equal to `{self.null_unless["value"]}`'
                )
            if self.has_default:
                writer.text(f'Default value: {self.default}.')
            else:
                writer.text('This argument has no default value.')
            c_key = f'{parent_name}.{self.name}'
            if c_key not in constraints:
                writer.text('There are no additional constraints on this argument.')
            else:
                writer.text('Additional constraints:')
                writer.itemize(
                    *(
                        f'Constraint on {join_items(constraint["arguments"])}: {constraint["description"]}'
                        for constraint in constraints[c_key]
                    )
                )


@dataclasses.dataclass
class Endpoint:
    name: str
    description: str 
    internal_use_only: bool 
    args: list[EndpointArgument]

    def write_markdown(self, writer: MarkdownWriter, constraints, argument_lists, dynamic_enums):
        with writer.file(f'./usage/dl_manager/dl_manager_endpoint__{self.name}.md'):
            writer.header(f'`{self.name}` Endpoint', size=1)
            writer.hrule()
            writer.text_bold(self.description)
            writer.hrule()
            if self.internal_use_only:
                writer.text_italic(
                    'This endpoint is used internally.',
                    'Such endpoints are used as an implementation detail of other endpoints.',
                    'Usually, the outward-facing endpoint retrieves a config from the database,'
                    ' and passes the arguments inside the config to the internal endpoint'
                )
                writer.hrule()
            writer.header('Arguments', size=2)
            for arg in self.args:
                arg.write_markdown(writer, constraints, argument_lists, self.name, dynamic_enums)



@dataclasses.dataclass
class BuilderParameter:
    name: str 
    description: str 
    arg_type: str 
    has_default: bool 
    default: typing.Any | None 
    readable_hint: str | None 
    minimum: str | None         # Numerical 
    maximum: str | None         # Numerical 
    options: list[str] | None   # enums 
    spec: dict[str, list[BuilderParameter]] | None     # nested 
    hyper_param_specs: list[str]

    def write_markdown(self, writer: MarkdownWriter):
        if self.spec is not None:
            return self.write_nested_args(writer)
        with writer.collapsible(self.name):
            writer.text_italic(self.description)
            match self.arg_type:
                case 'enum':
                    assert self.options is not None 
                    opts = ', '.join(f'`{x}`' for x in self.options)
                    writer.text(f'Argument type: enum (possible values: {opts})') 
                case 'float' | 'int':
                    match (self.minimum, self.maximum):
                        case (None, None):
                            writer.text(f'Argument type: {self.arg_type} (no restrictions)')
                        case (None, stop):
                            writer.text(f'Argument type: {self.arg_type} (maximum: {stop})')
                        case (start, None):
                            writer.text(f'Argument type: {self.arg_type} (minimum: {start})') 
                        case (start, stop):
                            writer.text(f'Argument type: {self.arg_type} (minimum: {start}, maximum: {stop})') 
                case _ as x:
                    writer.text(f'Argument type: {x}')
            if not self.has_default:
                writer.text('This argument has no default value')
            else:
                writer.text(f'Default value: {self.default}')
            writer.hrule()
            if self.hyper_param_specs:
                writer.text(f'Supported hyperparameter specs: {join_items([f"`{y}`" for y in self.hyper_param_specs])}')
            else:
                writer.text(f'No supported hyperparameter specs.')

    def write_nested_args(self, writer: MarkdownWriter):
        assert self.spec is not None 
        with writer.collapsible(self.name):
            writer.text_italic(self.description)
            writer.text('Argument type: nested arglist.')
            writer.text('Default values are inherited from contained child arguments.')
            writer.text('Hyper-parameter specs are inherited from nested child arguments.')
            writer.text_bold('Nested arguments:')
            for cat, args in self.spec.items():
                with writer.collapsible(cat):
                    for arg in args:
                        arg.write_markdown(writer)
            


##############################################################################
##############################################################################
# DL Manger Doc Generation 
##############################################################################


class MarkdownWriter:

    def __init__(self):
        self._files = collections.defaultdict(list)
        self._file = None 
        self._collapsible = []

    def flush(self):
        assert self._file is None 
        assert not self._collapsible 
        for filename, content in self._files.items():
            with open(filename, 'w') as file:
                file.write('\n'.join(content))

    @contextlib.contextmanager
    def file(self, filename: str):
        if self._collapsible:
            raise ValueError('Currently inside collapsible')
        self._file, old = filename, self._file  
        yield self 
        self._file = old 

    def _write(self, content: typing.Iterable[str]):
        if self._file is None:
            raise ValueError('No Markdown file specified')
        if self._collapsible:
            self._collapsible[-1].extend(content)
        else:
            self._files[self._file].extend(content)

    def header(self, text: str, size=1):
        if size < 1 or size > 6:
            raise ValueError(f'Invalid header size: {size}')
        self._write([f'{"#" * size} {text}'])

    def hrule(self):
        self._write(['', '---', ''])
    
    def text(self, *lines: str):
        self._write(lines)

    def text_bold(self, *lines: str):
        self._write(
            (f'**{line}**' for line in lines)
        )

    def text_italic(self, *lines: str):
        self._write(
            (f'_{line}_' for line in lines)
        )
    
    def itemize(self, *items: str):
        self._write(
            (f'- {item}' for item in items)
        )

    @contextlib.contextmanager
    def collapsible(self, title: str):
        #if self._collapsible is not None:
        #    raise ValueError('Currently inside collapsible')
        self._collapsible.append([])
        yield 
        stored = self._collapsible.pop(-1)
        self._write(['', '<details style="margin-left:2em">', f'<summary style="margin-left:-2em">{title}</summary>', ''])
        if not self._collapsible:
            def _interleave(x):
                for y in x:
                    yield ''
                    yield y 
                yield ''
        else:
            def _interleave(x):
                yield from x 
        self._write(_interleave(stored))
        self._write(['</details>', ''])
        

def retrieve_dl_argument_info(dl_manager_url: str, unsafe_ssl: bool):
    # Step 1: Get regular endpoint information 
    response = requests.get(f'{dl_manager_url}/endpoints', verify=not unsafe_ssl)
    response.raise_for_status()
    endpoints: list[Endpoint] = []
    for command in response.json()['commands']:
        ep = Endpoint(
            name=command['name'],
            description=command['help'],
            internal_use_only=command.get('private', False),
            args=[_retrieve_single_arg(arg) for arg in command['args']]
        ) 
        endpoints.append(ep)
    # Intermediate step: identify all arglists 
    arg_lists = []
    for ep in endpoints:
        for arg in ep.args:
            if arg.arg_type == 'arglist':
                arg_lists.append((ep.name, arg.name))
    # Step 2: Get arglist information
    argument_list_specs = {}
    for cmd, arg in arg_lists:
        response = requests.get(f'{dl_manager_url}/arglists/{cmd}/{arg}', verify=not unsafe_ssl)
        response.raise_for_status()
        spec = {
            name: _parse_single_arglist_part(value)
            for name, value in response.json().items()
        }
        argument_list_specs[f'{cmd}__{arg}'] = spec
    # Step 3: Get constraint information 
    response = requests.get(f'{dl_manager_url}/constraints', verify=not unsafe_ssl)
    response.raise_for_status()
    constraints = {}
    for constraint in response.json():
        for key in constraint['arguments']:
            constraints.setdefault(key, []).append(constraint)
    # Step 4: Get dynamic enums per endpoint 
    dynamic_enums = {}
    for ep in endpoints:
        response = requests.get(f'{dl_manager_url}/{ep.name}/dynamic-enums', 
                                verify=not unsafe_ssl)
        response.raise_for_status()
        dynamic_enums[ep.name] = response.json()
    return endpoints, argument_list_specs, constraints, dynamic_enums 


def _retrieve_single_arg(arg) -> EndpointArgument:
    logger.debug(f'Parsing argument: {arg["name"]}')
    return EndpointArgument(
        name=arg['name'],
        description=arg['help'],
        nargs=arg['nargs'],
        arg_type=arg['type'],
        required=arg['required'],
        options=arg['options'],
        has_default='default' in arg,
        default=arg.get('default', None),
        null_if=_parse_cond(arg['null-if']) if 'null-if' in arg else None,
        null_unless=_parse_cond(arg['null-unless']) if 'null-unless' in arg else None
    )


def _parse_cond(cond) -> ArgumentCondition:
    return ArgumentCondition(
        name=cond['name'],
        value=cond['value']
    )


def _parse_single_arglist_part(arg_list):
    return [
        BuilderParameter(
            name=item['name'],
            description=item['description'],
            arg_type=item['type'],
            has_default=item['has-default'],
            default=item['default'],
            readable_hint=x if (x := item['readable-options']) != {} else None,
            minimum=item.get('minimum', None),
            maximum=item.get('maximum', None),
            options=item.get('options', None),
            spec={
                name: _parse_single_arglist_part(value.values())
                for name, value in item['spec'].items()                
            } if 'spec' in item else None,
            hyper_param_specs=item['supported-hyper-param-specs'] 
        ) 
        for item in arg_list
    ]


def build_dl_manager_config_docs(dl_manager_url: str, unsafe_ssl: bool):
    logger.info('Building Deep Learning Manager User Documentation')
    logger.info('Retrieving argument information from DL manager')
    endpoints, arg_lists, constraints, dynamic_enums = retrieve_dl_argument_info(dl_manager_url, unsafe_ssl)
    logger.info('Writing Markdown')
    writer = MarkdownWriter()
    for ep in endpoints:
        ep.write_markdown(writer, constraints, arg_lists, dynamic_enums)
    for name, args in arg_lists.items():
        with writer.file(f'./usage/dl_manager/dl_manager_arglist__{name}.md'):
            writer.header(f'Arglist Documentation -- {name.replace("__", "/")}')
            writer.hrule()
            writer.header(f'Possible top-level items:', size=3)
            for opt_name, opt_args in args.items():
                target = f'./dl_manager_arglist__{name}__{opt_name}.md'
                writer.header(f'[{opt_name}]({target})', size=4)
                with writer.file(f'./usage/dl_manager/dl_manager_arglist__{name}__{opt_name}.md'):
                    writer.header(f'Parameters for {opt_name} options of arglist {name.replace("__", "/")}')
                    writer.hrule()
                    for arg in opt_args:
                        arg.write_markdown(writer)
                
    writer.flush()


##############################################################################
##############################################################################
# Main Function
##############################################################################

def main(dl_manager_url: str, unsafe_ssl: bool, java_path: str, plantuml_path: str):
    build_uml_files(java_path, plantuml_path) 
    build_dl_manager_config_docs(dl_manager_url, unsafe_ssl)


if __name__ == '__main__':
    # Setup argument parsing 
    parser = argparse.ArgumentParser('Maestro Documentation Builder', __doc__)
    parser.add_argument('--dl-manager-address',
                         type=str,
                         required=True,
                         help='Address of a running DL manager instance.')
    parser.add_argument('--allow-self-signed-certs',
                        action='store_true',
                        default=False,
                        help='Whether to allow unsafe SSL when connecting to the DL manager')
    parser.add_argument('--java-path',
                        type=str,
                        required=True,
                        help='Path to a Java executable used for building UML files.')
    parser.add_argument('--plantuml-path',
                        type=str,
                        required=True,
                        help='Path to a plantuml.jar file used for building UML files.')
    parser.add_argument('--log-level',
                        type=str,
                        default='info',
                        help='Logging level for the script. `debug`, `info`, `warning`, or `error`.')
    args = parser.parse_args()

    # Setup logging 
    logger = logging.getLogger('Maestro Doc Builder')
    formatter = logging.Formatter(
        '[{name}][{asctime}][{levelname}]: {msg}', style='{'
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    level = args.log_level
    levels = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR
    }
    if level not in levels:
        raise ValueError(f'Invalid logging leven: {level}')
    logger.setLevel(levels[level])

    # Invoke main script 
    main(args.dl_manager_address, args.allow_self_signed_certs, args.java_path, args.plantuml_path)

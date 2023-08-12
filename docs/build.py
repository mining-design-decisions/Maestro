"""
Utility script to help build Maestro's documentation.

Various parts of Maestro's documentation are automatically generated.
This script performs the required pre-flight checks and 
performs this generation.
"""

import argparse 
import logging 
import os 
import subprocess
import sys 


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


def main(dl_manager_url: str, java_path: str, plantuml_path: str):
    build_uml_files(java_path, plantuml_path) 


if __name__ == '__main__':
    # Setup argument parsing 
    parser = argparse.ArgumentParser('Maestro Documentation Builder', __doc__)
    parser.add_argument('--dl-manager-address',
                         type=str,
                         required=True,
                         help='Address of a running DL manager instance.')
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
    main(args.dl_manager_address, args.java_path, args.plantuml_path)

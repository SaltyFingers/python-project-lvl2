import json
import pathlib

import yaml


def get_dict(string, file_path):
    """
    Return dictionary from string representation of both files.
    arguments:
    first_string: string representation of first file
    second_string: string representation of second file
    suffix: extension of files
    """
    extension = pathlib.PurePosixPath(file_path).suffix

    if extension == '.json':
        return json.loads(string)

    elif extension in ['.yaml', '.yml']:
        return yaml.safe_load(string)

    else:
        raise TypeError('Wrong extension!')

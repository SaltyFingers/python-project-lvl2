import json

import yaml


def get_dict_from_string(string, extension):
    """
    Return dictionary from string representation of both files.
    arguments:
    first_string: string representation of first file
    second_string: string representation of second file
    suffix: extension of files
    """
    if extension == '.json':
        return json.loads(string)

    elif extension in ['.yaml', '.yml']:
        return yaml.safe_load(string)

    else:
        raise TypeError('Wrong extension!')

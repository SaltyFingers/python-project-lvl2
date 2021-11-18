from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish
from gendiff.search_difference import search_difference
from gendiff.parser import get_dict


def generate_diff(file_path1, file_path2, format='stylish'):
    """
    Return string representation of difference beween two files.
    arguments:
    file_path1: path to first file
    file_path2: path to second file
    format: selector of output format (default: stylish format)
    """

    dict1 = get_dict(get_string(file_path1), file_path1)
    dict2 = get_dict(get_string(file_path2), file_path2)

    difference = search_difference(dict1, dict2)

    if format == 'stylish':
        return format_stylish(difference)

    elif format == 'plain':
        return format_plain(difference)

    elif format == 'json':
        return format_json(difference)

    else:
        raise TypeError('Wrong format!')


def get_string(file_path):
    """
    Return string representation from file
    arguments:
    file_path: path to file to compare
    """

    with open(file_path, 'r') as file_object:
        string = file_object.read()
    return string

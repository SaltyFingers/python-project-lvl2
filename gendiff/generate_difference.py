import json
import pathlib

import yaml
from gendiff.formaters.json_formater import format_json
from gendiff.formaters.plain_formater import format_plain
from gendiff.formaters.stylish_formater import format_stylish
from gendiff.search_difference import search_difference


def generate_diff(file_path1, file_path2, format='stylish'):
    """
    Return string representation of difference beween two files.
    arguments:
    file_path1: path to first file
    file_path2: path to second file
    format: selector of output format (default: stylish format)
    """
    file1_extension = pathlib.PurePosixPath(file_path1).suffix
    file2_extension = pathlib.PurePosixPath(file_path2).suffix

    with open(file_path1, 'r') as first_object:
        first_dict = get_dict_from_string(first_object.read(),
                                          file1_extension)
    with open(file_path2, 'r') as second_object:
        second_dict = get_dict_from_string(second_object.read(),
                                           file2_extension)

    difference = search_difference(first_dict, second_dict)

    if format == 'stylish':
        return format_stylish(difference)

    if format == 'plain':
        return format_plain(difference)

    if format == 'json':
        return format_json(difference)


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

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

    with open(file_path1, 'r') as first_object:
        first_string = first_object.read()
    with open(file_path2, 'r') as second_object:
        second_string = second_object.read()

    file1_format = pathlib.PurePosixPath(file_path1).suffix
    file2_format = pathlib.PurePosixPath(file_path2).suffix

    first_dict = get_dict_from_string(first_string, file1_format)
    second_dict = get_dict_from_string(second_string, file2_format)

    difference = search_difference(first_dict, second_dict)

    if format == 'stylish':
        return format_stylish(difference)

    if format == 'plain':
        return format_plain(difference)

    if format == 'json':
        return format_json(difference)


def get_dict_from_string(string, suffix):
    """
    Return dictionary from string representation of both files.
    arguments:
    first_string: string representation of first file
    second_string: string representation of second file
    suffix: extension of files
    """
    if suffix == '.json':
        return json.loads(string)

    elif suffix in ['.yaml', '.yml']:
        return yaml.safe_load(string)

    else:
        raise TypeError('Wrong extension!')

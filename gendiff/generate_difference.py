import json
import pathlib

import yaml
from gendiff.search_difference import search_difference
from gendiff.formaters.stylish_formater import format_stylish
from gendiff.formaters.plain_formater import format_plain
from gendiff.formaters.json_formater import format_json


def generate_diff(file_path1, file_path2, format='stylish'):

    """Return string representation of difference beween two files.
    arguments:
    file_path1: path to first file
    file_path2: path to second file
    format: selector of output format (default: stylish format)
    """
    file1_format = pathlib.PurePosixPath(file_path1).suffix

    if file1_format == '.json':
        first_dict = json.load(open(file_path1))
        second_dict = json.load(open(file_path2))
    elif file1_format == '.yml' or file1_format == '.yaml':
        first_dict = yaml.safe_load(open(file_path1))
        second_dict = yaml.safe_load(open(file_path2))

    else:
        raise TypeError('Wrong extension!')

    difference = search_difference(first_dict, second_dict)

    if format == 'stylish':
        return format_stylish(difference)

    if format == 'plain':
        return format_plain(difference)

    if format == 'json':
        return format_json(difference)

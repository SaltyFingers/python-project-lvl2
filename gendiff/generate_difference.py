import json
import pathlib

import yaml
from gendiff.search_difference import search_difference
from gendiff.formaters.stylish_formater import format_stylish


def load_file_by_type(file_path):
    file_format = pathlib.PurePosixPath(file_path).suffix
    if file_format == '.json':
        file = json.load(open(file_path))
    elif file_format == '.yml' or file_format == '.yaml':
        file = yaml.safe_load(open(file_path))
    return file


def generate_diff(file_path1, file_path2, format):
    first_file, second_file = (load_file_by_type(file_path1),
                               load_file_by_type(file_path2))
    difference = search_difference(first_file, second_file)

    if format == 'stylish':
        return format_stylish(difference)
    # elif formater == '':
    #     return
    # elif formater == '':
    #     return

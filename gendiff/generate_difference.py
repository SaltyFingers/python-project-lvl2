import json
import pathlib

import yaml
from gendiff.search_difference import search_difference


def load_file_by_format(file_path):
    file_format = pathlib.PurePosixPath(file_path).suffix
    if file_format == '.json':
        file = json.load(open(file_path))
    elif file_format == '.yml' or file_format == '.yaml':
        file = yaml.safe_load(open(file_path))
    return file

def print_difference(difference):
    return difference


def generate_diff(file_path1, file_path2):
    first_file, second_file = (load_file_by_format(file_path1), 
                               load_file_by_format(file_path2))
    difference = search_difference(first_file, second_file)
    return print_difference(difference)



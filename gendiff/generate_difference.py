import json
import pathlib

import yaml
from gendiff.search_difference import search_difference


def get_encoded_bools(file):
    for key in file:
        if type(file[key]) == bool:
            file[key] = json.JSONEncoder().encode(file[key])

def load_file_by_format(file_path):
    file_format = pathlib.PurePosixPath(file_path).suffix
    if file_format == '.json':
        file = json.load(open(file_path))
    elif file_format == '.yml' or file_format == '.yaml':
        file = yaml.safe_load(open(file_path))
    return file

def print_difference(difference):
    result = '{}{}{}'.format('{\n', '\n'.join(difference), '\n}')
    return result


def generate_diff(file_path1, file_path2):
    first_file, second_file = (load_file_by_format(file_path1), 
                               load_file_by_format(file_path2))
    difference = search_difference(first_file, second_file)
    return print_difference(difference)



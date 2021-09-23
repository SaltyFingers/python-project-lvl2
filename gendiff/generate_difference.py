import json
import pathlib

import yaml
from gendiff.search_difference import search_difference


def get_encoded_bools(file):
    for key in file:
        if type(file[key]) == bool:
            file[key] = json.dumps(file[key])


def generate_diff(file_path1, file_path2):
    file1_format = pathlib.PurePosixPath(file_path1).suffix
    file2_format = pathlib.PurePosixPath(file_path2).suffix
    if file1_format == '.json':
        first_file = json.load(open(file_path1))
    elif file1_format == '.yml' or file1_format == '.yaml':
        first_file = yaml.safe_load(open(file_path1))
    if file2_format == '.json':
        second_file = json.load(open(file_path2))
    elif file2_format == '.yml' or file2_format == '.yaml':
        second_file = yaml.safe_load(open(file_path2))
    get_encoded_bools(first_file)
    get_encoded_bools(second_file)
    difference = search_difference(first_file, second_file)
    sorted_differense = sorted(difference, key=lambda x: x[4])
    result = '{\n' + '\n'.join(sorted_differense) + '\n}'
    return result

import pathlib

from gendiff.formaters.__init__ import select_formater
from gendiff.parser import get_dict
from gendiff.search_difference import search_difference


def generate_diff(file_path1, file_path2, format='stylish'):
    """
    Return string representation of difference beween two files.
    arguments:
    file_path1: path to first file
    file_path2: path to second file
    format: selector of output format (default: stylish format)
    """

    dict1 = get_dict(get_string(file_path1),
                     pathlib.PurePosixPath(file_path1).suffix)
    dict2 = get_dict(get_string(file_path2),
                     pathlib.PurePosixPath(file_path1).suffix)

    difference = search_difference(dict1, dict2)

    return select_formater(format)(difference)


def get_string(file_path):
    """
    Return string representation from file
    arguments:
    file_path: path to file to compare
    """

    with open(file_path, 'r') as file_object:
        string = file_object.read()
    return string

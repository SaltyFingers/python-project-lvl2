import pathlib

from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish
from gendiff.search_difference import search_difference
from gendiff.parser import get_dict_from_string


def generate_diff(file_path1, file_path2, format='stylish'):
    """
    Return string representation of difference beween two files.
    arguments:
    file_path1: path to first file
    file_path2: path to second file
    format: selector of output format (default: stylish format)
    """

    difference = search_difference(open_file_and_get_dict(file_path1),
                                   open_file_and_get_dict(file_path2))

    if format == 'stylish':
        return format_stylish(difference)

    if format == 'plain':
        return format_plain(difference)

    if format == 'json':
        return format_json(difference)


def open_file_and_get_dict(file_path):
    """
    Return dictionary from oppened file with it's path
    arguments:
    file_path: path to file to compare
    """

    file_extension = pathlib.PurePosixPath(file_path).suffix

    with open(file_path, 'r') as file_object:
        dict_from_string = get_dict_from_string(file_object.read(),
                                                file_extension)
    return dict_from_string

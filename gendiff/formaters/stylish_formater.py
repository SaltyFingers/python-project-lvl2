from json import JSONEncoder

from gendiff.search_difference import is_dictionary


def encode_value(value):

    """Returns encoded value if it necessary"""

    if type(value) == bool or value is None:
        return JSONEncoder().encode(value)
    return value


def format_stylish(diff, depth=0):

    """Returns formated difference between two files

    arguments:
    diff: raw differene between two files
    depth: level of nesting to build correct difference"""

    if not is_dictionary(diff):
        return encode_value(diff)

    keys = sorted(diff.keys())
    indent = " " * depth
    difference = ['{']
    depth += 4

    for key in keys:
        add_formated_object(key, diff, indent, depth, difference)

    difference.append(f'{indent}}}')
    return '\n'.join(difference)


def add_formated_object(key, diff, indent, depth, difference):

    """Add formated object to formated difference in depending of it's condition

    arguments:
    key: current key in diff
    diff: part of full difference (value)
    indent: indent in dictionary
    depth: level of nesting in that moment
    difference: formated difference"""

    if diff[key]['condition'] == 'deleted':
        obj = (f'{indent}  - {key}: '
               f'{format_stylish(diff[key]["value"], depth)}')

    elif diff[key]['condition'] == 'added':
        obj = (f'{indent}  + {key}: '
               f'{format_stylish(diff[key]["value"], depth)}')

    elif diff[key]['condition'] == 'not changed':
        obj = (f'{indent}    {key}: '
               f'{format_stylish(diff[key]["value"], depth)}')

    elif diff[key]['condition'] == 'updated':
        obj = (f'{indent}  - {key}: '
               f'{format_stylish(diff[key]["value1"], depth)}\n'
               f'{indent}  + {key}: '
               f'{format_stylish(diff[key]["value2"], depth)}')

    elif diff[key]['children']:
        obj = (f'{indent}    {key}: '
               f'{format_stylish(diff[key]["children"], depth)}')

    difference.append(obj)

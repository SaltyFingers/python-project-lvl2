from json import JSONEncoder

from gendiff.search_difference import is_dictionary


def format_value(value):

    """Returns formated value if it necessary"""

    if type(value) == bool or value is None:
        return JSONEncoder().encode(value)
    return str(value)


def format_stylish(diff, depth=0):
    """Returns formated difference between two files in stylish format

    arguments:
    diff: raw differene between two files
    depth: level of nesting to build correct difference"""

    indent = " " * depth
    difference = ['{']
    keys = diff.keys()
    for key in keys:
        strings = map(lambda key: get_formated_object(
                      key, diff, indent, depth), keys)
        obj = '\n'.join(strings)
    difference.append(obj)
    difference.append(f'{indent}}}')
    return '\n'.join(difference)


def get_formated_object(key, diff, indent, depth):

    """Add formated object to formated difference in depending of it's condition

    arguments:
    key: current key in diff
    diff: part of full difference (value)
    indent: indent in dictionary
    depth: level of nesting in that moment
    difference: formated difference"""

    condition = diff[key]['condition']

    if condition == 'deleted':
        obj = (f'{indent}  - {key}: '
               f'{format_nested_object(diff[key]["value"], depth + 4)}')

    elif condition == 'added':
        obj = (f'{indent}  + {key}: '
               f'{format_nested_object(diff[key]["value"], depth + 4)}')

    elif condition == 'not changed':
        obj = (f'{indent}    {key}: '
               f'{format_nested_object(diff[key]["value"], depth + 4)}')

    elif condition == 'updated':
        obj = (f'{indent}  - {key}: '
               f'{format_nested_object(diff[key]["value1"], depth + 4)}\n'
               f'{indent}  + {key}: '
               f'{format_nested_object(diff[key]["value2"], depth + 4)}')
    elif condition == 'nested':
        obj = (f'{indent}    {key}: '
               f'{format_stylish(diff[key]["children"], depth + 4)}')
    return obj


def format_nested_object(diff, depth):
    indent = ' ' * depth
    nested_diff = []
    if is_dictionary(diff):
        nested_diff.append('{')
        keys = diff.keys()
        for key in keys:
            obj = (f'{indent}    {key}: '
                   f'{format_nested_object(diff[key], depth + 4)}')
            nested_diff.append(obj)
        nested_diff.append(f'{indent}}}')
    else:
        obj = format_value(diff)
        nested_diff.append(obj)
    return '\n'.join(nested_diff)

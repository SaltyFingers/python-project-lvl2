from json import JSONEncoder

from gendiff.search_difference import is_dictionary

prefixes = {
    'removed': '  - ',
    'added': '  + ',
    'not changed': '    ',
    'updated': '    ',
    'nested': '    '
}


def format_value(value, depth=0):
    """Returns formated value if it necessary"""
    if type(value) == bool or value is None:
        return JSONEncoder().encode(value)
    elif is_dictionary(value):
        return get_string_from_dictionary(value, depth + 1)
    return str(value)


def format_stylish(diff, depth=0):
    """
    Returns formated difference between two files in stylish format
    arguments:
    diff: raw differene between two files
    depth: level of nesting to build correct difference
    """
    indent = '    ' * depth
    difference = ['{']
    keys = diff.keys()

    for key in keys:
        status = diff[key]['status']
        string = get_formated_string(indent, status, diff, key, depth)
        difference.append(string)
    difference.append(f'{indent}}}')
    return '\n'.join(difference)


def get_formated_string(indent, status, diff, key, depth):
    """
    Return formated string in dependence of node's status
    arguments:
    indent: amount of whitespaces to build stylish representation
    status: status of node
    diff: difference between two files
    key: current key
    depth: node's level of nesting
    """
    if status == 'added':
        string = (f'{indent}{prefixes["added"]}{key}: '
                  f'{format_value(diff[key]["value"], depth)}')

    elif status == 'removed':
        string = (f'{indent}{prefixes["removed"]}{key}: '
                  f'{format_value(diff[key]["value"], depth)}')

    elif status == 'not changed':
        string = (f'{indent}{prefixes["not changed"]}{key}: '
                  f'{format_value(diff[key]["value"], depth)}')

    elif status == 'updated':
        string = (f'{indent}{prefixes["removed"]}{key}: '
                  f'{format_value(diff[key]["value1"], depth)}\n'
                  f'{indent}{prefixes["added"]}{key}: '
                  f'{format_value(diff[key]["value2"], depth)}')

    elif status == 'nested':
        string = (f'{indent}{prefixes[status]}{key}: '
                  f'{format_stylish(diff[key]["children"], depth + 1)}')
    return string


def get_string_from_dictionary(diff, depth):
    """
    Return string representation of value if it's dictionary
    arguments:
    diff: difference between two files
    depth: node's level of nesting
    """
    indent = '    ' * depth
    nested_diff = []
    if is_dictionary(diff):
        nested_diff.append('{')
        keys = diff.keys()
        for key in keys:
            string = (f'{indent}{prefixes["not changed"]}{key}: '
                      f'{get_string_from_dictionary(diff[key], depth + 1)}')
            nested_diff.append(string)
        nested_diff.append(f'{indent}}}')
    else:
        string = format_value(diff, depth)
        nested_diff.append(string)
    return '\n'.join(nested_diff)

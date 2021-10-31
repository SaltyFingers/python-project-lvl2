from json import JSONEncoder

from gendiff.search_difference import is_dictionary


prefixes = {
    'removed': '  - ',
    'added': '  + ',
    'not changed': '    ',
    'updated': '    ',
    'nested': '    '
}


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

    indent = '    ' * depth
    difference = ['{']
    keys = diff.keys()

    for key in keys:

        status = diff[key]['status']

        if status == 'updated':
            obj = (f'{indent}{prefixes["removed"]}{key}: '
                   f'{format_nested_object(diff[key]["value1"], depth + 1)}\n'
                   f'{indent}{prefixes["added"]}{key}: '
                   f'{format_nested_object(diff[key]["value2"], depth + 1)}')

        elif status == 'nested':
            obj = (f'{indent}{prefixes[status]}{key}: '
                   f'{format_stylish(diff[key]["children"], depth + 1)}')

        else:
            obj = (f'{indent}{prefixes[status]}{key}: '
                   f'{format_nested_object(diff[key]["value"], depth + 1)}')

        difference.append(obj)
    difference.append(f'{indent}}}')
    return '\n'.join(difference)


def format_nested_object(diff, depth):
    indent = '    ' * depth
    nested_diff = []
    if is_dictionary(diff):
        nested_diff.append('{')
        keys = diff.keys()
        for key in keys:
            obj = (f'{indent}{prefixes["not changed"]}{key}: '
                   f'{format_nested_object(diff[key], depth + 1)}')
            nested_diff.append(obj)
        nested_diff.append(f'{indent}}}')
    else:
        obj = format_value(diff)
        nested_diff.append(obj)
    return '\n'.join(nested_diff)

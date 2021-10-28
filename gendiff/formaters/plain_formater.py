from json import JSONEncoder

from gendiff.search_difference import is_dictionary


def format_value(value):

    """Returns formated value if it necessary"""

    if type(value) == bool or value is None:
        return JSONEncoder().encode(value)
    elif is_dictionary(value):
        return '[complex value]'
    elif type(value) == int:
        return value
    else:
        return f"'{value}'"


def format_plain(diff, path=''):

    """Returns formated difference between two files if plain format

    arguments:
    diff: raw differene between two files
    path: path to value (default: '') using to build full path"""

    keys = sorted(diff.keys())
    difference = []

    for key in keys:
        full_path = path
        if diff[key]['status'] == 'not changed':
            obj = ''
        elif diff[key]['status'] == 'nested':
            full_path += (f'{key}.')
            obj = format_plain(diff[key]['children'], full_path)
        else:
            status = diff[key]['status']
            full_path += (f'{key}')
            obj = get_formated_object(key, diff, full_path, status)
        if obj:
            difference.append(obj)

    return '\n'.join(difference)


def get_formated_object(key, diff, full_path, status):

    """Make string in depending of value's status

    arguments:
    key: current key in diff
    diff: part of full difference (value)
    full_path: full path to value
    status: status of value in diff"""

    if status == 'removed':
        return (f"Property '{full_path}' was removed")
    elif status == 'added':
        return (f"Property '{full_path}' "
                f"was added with value: {format_value(diff[key]['value'])}")
    elif status == 'updated':
        return (f"Property '{full_path}' was updated. "
                f"From {format_value(diff[key]['value1'])} "
                f"to {format_value(diff[key]['value2'])}")

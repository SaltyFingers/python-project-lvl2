from json import JSONEncoder

from gendiff.search_difference import is_dictionary


def decode_value(value):
    if type(value) == bool or value is None:
        return JSONEncoder().encode(value)
    elif is_dictionary(value):
        return '[complex value]'
    else:
        return f"'{value}'"


def format_plain(diff, path=''):

    keys = sorted(diff.keys())
    difference = []

    for key in keys:
        full_path = path
        add_formated_object(key, diff, difference, full_path)

    return '\n'.join(difference)


def get_formated_object(key, diff, full_path, condition):
    if condition == 'deleted':
        return (f"Property '{full_path}' was removed")
    elif condition == 'added':
        return (f"Property '{full_path}' "
                f"was added with value: {decode_value(diff[key]['value'])}")
    elif condition == 'updated':
        return (f"Property '{full_path}' was updated. "
                f"From {decode_value(diff[key]['value1'])} "
                f"to {decode_value(diff[key]['value2'])}")


def add_formated_object(key, diff, difference, full_path):
    if diff[key]['condition'] == 'not changed':
        obj = ''
    elif diff[key]['condition'] == 'changed':
        full_path += (f'{key}.')
        obj = format_plain(diff[key]['children'], full_path)
    else:
        condition = diff[key]['condition']
        full_path += (f'{key}')
        obj = get_formated_object(key, diff, full_path, condition)
    if obj:
        difference.append(obj)

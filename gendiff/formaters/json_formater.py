from json import JSONEncoder

from gendiff.search_difference import is_dictionary


def decode_value(value):
    return JSONEncoder().encode(value)


def format_json(diff):

    if not is_dictionary(diff):
        return decode_value(diff)

    keys = sorted(diff.keys())
    difference = ['{']
    count = 0

    for key in keys:
        add_formated_object(key, diff, difference)
        count += 1
        if count < len(keys):
            difference.append(', ')

    difference.append('}')
    return ''.join(difference)


def add_formated_object(key, diff, difference):
    condition = diff[key]['condition']

    if condition == 'deleted':
        obj = (f'"{key}": {{"condition": "{condition}", "value": '
               f'{format_json(diff[key]["value"])}}}')

    elif condition == 'added':
        obj = (f'"{key}": {{"condition": "{condition}", "value": '
               f'{format_json(diff[key]["value"])}}}')

    elif condition == 'not changed':
        obj = (f'"{key}": {{"condition": "{condition}", "value": '
               f'{format_json(diff[key]["value"])}}}')

    elif condition == 'updated':
        obj = (f'"{key}": {{"condition": "{condition}", "value1": '
               f'{format_json(diff[key]["value1"])}, "value2": '
               f'{format_json(diff[key]["value2"])}}}')

    elif diff[key]['children']:
        obj = (f'"{key}": {{"condition": "{condition}", "value": '
               f'{format_json(diff[key]["children"])}}}')

    difference.append(obj)

from json import JSONEncoder

from gendiff.search_difference import is_dictionary


def encode_value(value):

    """Returns encoded value"""

    return JSONEncoder().encode(value)


def format_json(diff):

    """Returns formated difference between two files if json format

    arguments:
    diff: raw differene between two files"""

    keys = sorted(diff.keys())
    difference = ['{']

    for key in keys:
        strings = map(lambda key: add_formated_object(
                      key, diff), keys)
        obj = ', '.join(strings)

    difference.append(obj)
    difference.append('}')
    return ''.join(difference)


def add_formated_object(key, diff):

    """Add formated object to formated difference in depending of it's condition

    arguments:
    key: current key in diff
    diff: part of full difference (value)
    difference: formated difference"""

    condition = diff[key]['condition']

    if condition == 'deleted':
        obj = (f'"{key}": {{"condition": "{condition}", "value": '
               f'{format_nested_object(diff[key]["value"])}}}')

    elif condition == 'added':
        obj = (f'"{key}": {{"condition": "{condition}", "value": '
               f'{format_nested_object(diff[key]["value"])}}}')

    elif condition == 'not changed':
        obj = (f'"{key}": {{"condition": "{condition}", "value": '
               f'{format_nested_object(diff[key]["value"])}}}')

    elif condition == 'updated':
        obj = (f'"{key}": {{"condition": "{condition}", "value1": '
               f'{format_nested_object(diff[key]["value1"])}, "value2": '
               f'{format_nested_object(diff[key]["value2"])}}}')

    elif condition == 'nested':
        obj = (f'"{key}": {{"condition": "{condition}", "children": '
               f'{format_json(diff[key]["children"])}}}')

    return obj


def format_nested_object(diff):
    nested_diff = []
    if is_dictionary(diff):
        nested_diff.append('{')
        keys = diff.keys()
        count = 0
        for key in keys:
            obj = (f'"{key}": '
                   f'{format_nested_object(diff[key])}')
            nested_diff.append(obj)
            count += 1
            if count < len(keys):
                nested_diff.append(', ')
            elif count == len(keys):
                nested_diff.append('}')
    else:
        obj = encode_value(diff)
        nested_diff.append(obj)
    return ''.join(nested_diff)

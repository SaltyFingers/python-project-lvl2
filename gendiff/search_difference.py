from json import JSONEncoder


def is_dictionary(object):
    return isinstance(object, dict)


def decode_value(value):
    if type(value) == bool or value is None:
        return JSONEncoder().encode(value)
    else:
        return str(value)


def get_keys(dict1, dict2):
    first_keys = list(dict1.keys())
    second_keys = list(dict2.keys())
    return set(first_keys + second_keys)


def add_object(key, dict1, dict2, difference):
    if key in dict1 and key not in dict2:
        difference[key] = {
            'condition': 'deleted',
            'children': None,
            'value': search_difference(dict1[key]),
        }

    elif key in dict2 and key not in dict1:
        difference[key] = {
            'condition': 'added',
            'children': None,
            'value': search_difference(dict2[key]),
        }

    else:

        if dict1[key] == dict2[key]:
            difference[key] = {
                'condition': 'equal',
                'children': None,
                'value': search_difference(dict1[key]),
            }

        elif not is_dictionary(dict1[key]) or not is_dictionary(dict2[key]):
            difference[key] = {
                'condition': 'replaced',
                'children': None,
                'value1': search_difference(dict1[key]),
                'value2': search_difference(dict2[key]),
            }

        elif is_dictionary(dict1[key]) and is_dictionary(dict2[key]):
            difference[key] = {
                'condition': 'changed',
                'children': (search_difference(dict1[key], dict2[key])),
                'value': None,
            }


def search_difference(dict1, dict2=None):
    if not is_dictionary(dict1):
        return dict1

    if dict2 is None:
        dict2 = dict1

    keys = sorted(get_keys(dict1, dict2))

    difference = {}

    for key in keys:
        add_object(key, dict1, dict2, difference)

    return difference

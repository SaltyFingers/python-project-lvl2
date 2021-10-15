def is_dictionary(object):

    """Return True if object is dictionary, of False if not."""

    return isinstance(object, dict)


def get_keys(dict1, dict2):

    """Return set of keys in two dictionaries.
    arguments:
    dict1: first dictionary
    dict2: second dictionary
    """

    first_keys = list(dict1.keys())
    second_keys = list(dict2.keys())
    return set(first_keys + second_keys)


def add_object(key, dict1, dict2, difference):

    """Add object to raw difference.
    arguments:
    key: current key in dictionary(ies)
    dict1: first dictionary
    dict2: second dictionary
    difference: raw difference
    """

    if key in dict1 and key not in dict2:
        difference[key] = {
            'condition': 'deleted',
            'value': search_difference(dict1[key]),
        }

    elif key in dict2 and key not in dict1:
        difference[key] = {
            'condition': 'added',
            'value': search_difference(dict2[key]),
        }

    elif dict1[key] == dict2[key]:
        difference[key] = {
            'condition': 'not changed',
            'value': search_difference(dict1[key]),
        }

    elif not is_dictionary(dict1[key]) or not is_dictionary(dict2[key]):
        difference[key] = {
            'condition': 'updated',
            'value1': search_difference(dict1[key]),
            'value2': search_difference(dict2[key]),
        }

    elif is_dictionary(dict1[key]) and is_dictionary(dict2[key]):
        difference[key] = {
            'condition': 'changed',
            'children': (search_difference(dict1[key], dict2[key])),
        }


def search_difference(dict1, dict2=None):

    """Return raw difference between two dictionaries (files).
    arguments:
    dict1: first dictionary
    dict2: second dictionary (default: None if key only in one dictionary)
    """

    if not is_dictionary(dict1):
        return dict1

    if dict2 is None:
        dict2 = dict1

    keys = sorted(get_keys(dict1, dict2))

    difference = {}

    for key in keys:
        add_object(key, dict1, dict2, difference)

    return difference

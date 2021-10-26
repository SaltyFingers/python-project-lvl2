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


def search_difference(dict1, dict2):

    """Return raw difference between two dictionaries (files).
    arguments:
    dict1: first dictionary
    dict2: second dictionary (default: None if key only in one dictionary)
    """

    keys = sorted(get_keys(dict1, dict2))
    difference = {}

    for key in keys:
        if key in dict1 and key not in dict2:
            difference[key] = {
                'condition': 'deleted',
                'value': dict1.get(key),
            }

        elif key in dict2 and key not in dict1:
            difference[key] = {
                'condition': 'added',
                'value': dict2.get(key),
            }

        elif dict1[key] == dict2[key]:
            difference[key] = {
                'condition': 'not changed',
                'value': dict1.get(key),
            }

        elif not is_dictionary(dict1[key]) or not is_dictionary(dict2[key]):
            difference[key] = {
                'condition': 'updated',
                'value1': dict1.get(key),
                'value2': dict2.get(key),
            }

        elif is_dictionary(dict1[key]) and is_dictionary(dict2[key]):
            difference[key] = {
                'condition': 'nested',
                'children': (search_difference(dict1[key], dict2[key])),
            }
    return difference

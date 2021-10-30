def is_dictionary(object):

    """Return True if object is dictionary, of False if not."""
    return isinstance(object, dict)


def is_nested(object1, object2):
    return isinstance(object1, dict) and isinstance(object2, dict)


def get_keys(dict1, dict2):
    """
    Return set of keys in two dictionaries.
    arguments:
    dict1: first dictionary
    dict2: second dictionary
    """
    return set(list(dict1.keys()) + list(dict2.keys()))


def search_difference(dict1, dict2):
    """
    Return raw difference between two dictionaries (files).
    arguments:
    dict1: first dictionary
    dict2: second dictionary
    """
    keys = sorted(get_keys(dict1, dict2))
    difference = {}

    for key in keys:

        status = get_status(dict1, dict2, key)
        values = get_value(dict1, dict2, key, status['status'])
        difference[key] = status
        difference[key].update(values)

    return difference


def get_status(dict1, dict2, key):
    """
    Return status of key in difference.
    arguments:
    dict1: first dictionary
    dict2: second dictionary
    key: current key
    """
    if key in dict1 and key not in dict2:
        status = {'status': 'removed'}
    elif key in dict2 and key not in dict1:
        status = {'status': 'added'}
    elif dict1[key] == dict2[key]:
        status = {'status': 'not changed'}
    elif not is_dictionary(dict1[key]) or not is_dictionary(dict2[key]):
        status = {'status': 'updated'}
    elif is_nested(dict1[key], dict2[key]):
        status = {'status': 'nested'}
    return status


def get_value(dict1, dict2, key, status):
    """
    Return value of key in difference.
    arguments:
    dict1: first dictionary
    dict2: second dictionary
    key: current key
    status: status of key in difference
    """
    if status == 'removed':
        value = {'value': dict1.get(key)}
    elif status == 'added':
        value = {'value': dict2.get(key)}
    elif status == 'not changed':
        value = {'value': dict1.get(key)}
    elif status == 'updated':
        value = {'value1': dict1.get(key), 'value2': dict2.get(key)}
    elif status == 'nested':
        value = {'children': search_difference(dict1[key], dict2[key])}
    return value

from gendiff.search_difference import (
    get_keys,
    is_dictionary,
    search_difference,
)


def test_is_dictionary():
    assert is_dictionary({"key": "value", "not_key": "not_value"}) is True
    assert is_dictionary("100_percent_dictionary") is False


def test_get_keys():
    dict1 = {"a": "aa", "b": "bb"}
    dict2 = {"b": "bb", "c": "cc"}
    assert get_keys(dict1, dict2) == {"a", "b", "c"}


def test_search_difference():
    dict1 = {"a": "aa", "b": "bb", "d": {"dd": "ddd"}}
    dict2 = {"b": "bbb", "c": "cc", "d": {"dd": "dddd"}}
    expectation = (
    {'a': {'condition': 'deleted', 'children': None, 'value': 'aa'},  # noqa
     'b': {'condition': 'updated', 'children': None, 'value1': 'bb',
           'value2': 'bbb'},
     'c': {'condition': 'added', 'children': None, 'value': 'cc'},
     'd': {'condition': 'changed', 'children':
           {'dd': {'condition': 'updated', 'children': None,
                   'value1': 'ddd', 'value2': 'dddd'}}, 'value': None}
     })
    assert search_difference(dict1, dict2) == expectation

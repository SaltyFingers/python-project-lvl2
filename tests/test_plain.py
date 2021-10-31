import pytest
from gendiff.formaters.plain_formater import format_value, get_formated_object

FILEPATH_JSON1 = 'tests/fixtures/file1_2.json'
FILEPATH_JSON2 = 'tests/fixtures/file2_2.json'
FILEPATH_YAML1 = 'tests/fixtures/file1_2.yaml'
FILEPATH_YAML2 = 'tests/fixtures/file2_2.yaml'


def test_decoding_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value({'a': 'b'}) == '[complex value]'
    assert format_value(300) == 300


@pytest.mark.parametrize('key, diff, full_path, status, expected', [
    ('follow', {'follow': {'condition': 'added', 'value': False}},
     'common.follow', 'added',
     "Property 'common.follow' was added with value: false"),
    ('setting3',
     {'setting3': {'condition': 'updated', 'value1': True, 'value2': None}},
     'common.setting3', 'updated',
     "Property 'common.setting3' was updated. From true to null")])
def test_get_formated_object(key, diff, full_path, status, expected):
    assert get_formated_object(key, diff, full_path, status) == expected

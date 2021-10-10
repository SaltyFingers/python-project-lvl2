import pytest
from gendiff.generate_diff import generate_diff
from gendiff.formaters.json_formater import decode_value


def test_encoding():
    assert decode_value(False) == "false"
    assert decode_value(None) == "null"


@pytest.fixture
def json_json_file_path1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def json_json_file_path2():
    return 'tests/fixtures/file2.json'


def test_stylish_json(json_json_file_path1,
                      json_json_file_path2):
    expectation = (
"""{"follow": {"condition": "deleted", "value": false}, "host": {"condition": "not changed", "value": "hexlet.io"}, \
"proxy": {"condition": "deleted", "value": "123.234.53.22"}, "timeout": {"condition": "updated", "value1": 50, "value2": 20}, \
"verbose": {"condition": "added", "value": true}}""")
    assert generate_diff(json_json_file_path1,
                         json_json_file_path2, 'json') == expectation


@pytest.fixture
def json_yaml_file_path1():
    return 'tests/fixtures/file1.yaml'


@pytest.fixture
def json_yaml_file_path2():
    return 'tests/fixtures/file2.yaml'


def test_stylish_yaml(json_yaml_file_path1,
                      json_yaml_file_path2):
    expectation = (
"""{"follow": {"condition": "deleted", "value": false}, "host": {"condition": "not changed", "value": "hexlet.io"}, \
"proxy": {"condition": "deleted", "value": "123.234.53.22"}, "timeout": {"condition": "updated", "value1": 50, "value2": 20}, \
"verbose": {"condition": "added", "value": true}}""")
    assert generate_diff(json_yaml_file_path1,
                         json_yaml_file_path2, 'json') == expectation
import pytest
from gendiff.generate_difference import generate_diff, load_file_by_extension


@pytest.fixture
def json_file_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def yaml_file_path():
    return 'tests/fixtures/file2.yaml'


def test_json_file_opening(json_file_path):
    expectation = {"host": "hexlet.io", "timeout": 50,
                   "proxy": "123.234.53.22", "follow": False}
    assert load_file_by_extension(json_file_path) == expectation


def test_yaml_file_opening(yaml_file_path):
    expectation = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    assert load_file_by_extension(yaml_file_path) == expectation


@pytest.fixture
def plain_json_file_path1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def plain_json_file_path2():
    return 'tests/fixtures/file2.json'


def test_default_format(plain_json_file_path1, plain_json_file_path2):
    assert (generate_diff(plain_json_file_path1,
                          plain_json_file_path2) == generate_diff(
            plain_json_file_path1, plain_json_file_path2, 'stylish'))

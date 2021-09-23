import pytest
from gendiff.generate_difference import generate_diff


@pytest.fixture
def json_file_path1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def json_file_path2():
    return 'tests/fixtures/file2.json'


def test_json(json_file_path1, json_file_path2):
    exceptation = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(json_file_path1, json_file_path2) == exceptation


@pytest.fixture
def yaml_file_path1():
    return 'tests/fixtures/file1.yaml'


@pytest.fixture
def yaml_file_path2():
    return 'tests/fixtures/file2.yaml'


def test_yaml(yaml_file_path1, yaml_file_path2):
    exceptation = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(yaml_file_path1, yaml_file_path2) == exceptation

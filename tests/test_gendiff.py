import pytest
from gendiff.generate_difference import generate_diff


@pytest.fixture
def plain_json_file_path1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def plain_json_file_path2():
    return 'tests/fixtures/file2.json'


def test_plain_json(plain_json_file_path1, plain_json_file_path2):
    exceptation = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(plain_json_file_path1,
                         plain_json_file_path2) == exceptation


@pytest.fixture
def plain_yaml_file_path1():
    return 'tests/fixtures/file1.yaml'


@pytest.fixture
def plain_yaml_file_path2():
    return 'tests/fixtures/file2.yaml'


def test_plain_yaml(plain_yaml_file_path1, plain_yaml_file_path2):
    exceptation = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(plain_yaml_file_path1,
                         plain_yaml_file_path2) == exceptation


@pytest.fixture
def stylish_json_file_path1():
    return


@pytest.fixture
def stylish_json_file_path2():
    return


def test_stylish_json(stylish_json_file_path1,
                      stylish_json_file_path2):
    exceptation = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert generate_diff(stylish_json_file_path1,
                         stylish_json_file_path2) == exceptation


@pytest.fixture
def stylish_yaml_file_path1():
    return


@pytest.fixture
def stylish_yaml_file_path2():
    return


def test_stylish_yaml(stylish_yaml_file_path1,
                      stylish_yaml_file_path2):
    exceptation = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert generate_diff(stylish_yaml_file_path1,
                         stylish_yaml_file_path2) == exceptation
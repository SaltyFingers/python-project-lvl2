from gendiff.formaters.json_formater import encode_value
from gendiff.generate_difference import generate_diff

FILEPATH_JSON1 = 'tests/fixtures/file1_2.json'
FILEPATH_JSON2 = 'tests/fixtures/file2_2.json'
FILEPATH_YAML1 = 'tests/fixtures/file1_2.yaml'
FILEPATH_YAML2 = 'tests/fixtures/file2_2.yaml'


def test_encoding():
    assert encode_value(False) == "false"
    assert encode_value(None) == "null"


def test_stylish_json():
    expectation = open('tests/fixtures/expectation_json.txt', 'r').read()
    assert generate_diff(FILEPATH_JSON1,
                         FILEPATH_JSON2, 'json') == expectation


def test_stylish_yaml():
    expectation = open('tests/fixtures/expectation_json.txt', 'r').read()
    assert generate_diff(FILEPATH_YAML1,
                         FILEPATH_YAML2, 'json') == expectation

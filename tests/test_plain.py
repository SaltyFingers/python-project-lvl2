from gendiff.formaters.plain_formater import format_value
import pytest
from gendiff.generate_difference import generate_diff


FILEPATH_JSON1 = 'tests/fixtures/file1_2.json'
FILEPATH_JSON2 = 'tests/fixtures/file2_2.json'
FILEPATH_YAML1 = 'tests/fixtures/file1_2.yaml'
FILEPATH_YAML2 = 'tests/fixtures/file2_2.yaml'


def test_plain_json():
    expectation = open('tests/fixtures/expectation_plain.txt', 'r').read()
    assert generate_diff(FILEPATH_JSON1,
                         FILEPATH_JSON2, 'plain') == expectation



def test_plain_yaml():
    expectation = open('tests/fixtures/expectation_plain.txt', 'r').read()
    assert generate_diff(FILEPATH_YAML1,
                         FILEPATH_YAML2, 'plain') == expectation


def test_decoding_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value({'a': 'b'}) == '[complex value]'
    assert format_value(300) == 300

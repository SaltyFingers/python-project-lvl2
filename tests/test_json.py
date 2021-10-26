from gendiff.generate_difference import generate_diff
import pytest

FILEPATH_JSON1 = 'tests/fixtures/file1_2.json'
FILEPATH_JSON2 = 'tests/fixtures/file2_2.json'
FILEPATH_YAML1 = 'tests/fixtures/file1_2.yaml'
FILEPATH_YAML2 = 'tests/fixtures/file2_2.yaml'

@pytest.mark.parametrize('path1, path2, expected', [
    (FILEPATH_JSON1, FILEPATH_JSON2, 
     open('tests/fixtures/expectation_json.txt', 'r').read()),
    (FILEPATH_YAML1, FILEPATH_YAML2, 
     open('tests/fixtures/expectation_json.txt', 'r').read())])
def test_opening(path1, path2, expected):
    assert generate_diff(path1, path2, 'json') == expected

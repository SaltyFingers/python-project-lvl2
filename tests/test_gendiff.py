import pytest
from gendiff.generate_difference import generate_diff, load_file_by_extension

FILEPATH_JSON1 = 'tests/fixtures/file1.json'
FILEPATH_JSON2 = 'tests/fixtures/file2.json'
FILEPATH_YAML = 'tests/fixtures/file2.yaml'
FILEPATH_WRONG = 'tests/fixtures/expectation_json.txt'


@pytest.mark.parametrize('test_input, expected', [
    (FILEPATH_JSON1, {"host": "hexlet.io", "timeout": 50,
                      "proxy": "123.234.53.22", "follow": False}),
    (FILEPATH_YAML, {"timeout": 20, "verbose": True, "host": "hexlet.io"})])
def test_opening(test_input, expected):
    assert load_file_by_extension(test_input) == expected

    with pytest.raises(Exception):
        load_file_by_extension(FILEPATH_WRONG)


def test_wrong_file_gendiff():
    with pytest.raises(Exception):
        generate_diff(FILEPATH_WRONG, FILEPATH_WRONG)


def test_default_format():
    assert (generate_diff(FILEPATH_JSON1,
                          FILEPATH_JSON2) == generate_diff(
            FILEPATH_JSON1, FILEPATH_JSON2, 'stylish'))

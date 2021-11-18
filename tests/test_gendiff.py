import pytest
from gendiff.generate_difference import generate_diff

FILEPATH_JSON1 = 'tests/fixtures/file1.json'
FILEPATH_JSON2 = 'tests/fixtures/file2.json'
FILEPATH_JSON1_2 = 'tests/fixtures/file1_2.json'
FILEPATH_JSON2_2 = 'tests/fixtures/file2_2.json'
FILEPATH_YAML = 'tests/fixtures/file2.yaml'
FILEPATH_YAML1_2 = 'tests/fixtures/file1_2.yaml'
FILEPATH_YAML2_2 = 'tests/fixtures/file2_2.yaml'
FILEPATH_WRONG = 'tests/fixtures/expectation_json.txt'
EXPECTATION_STYLISH = 'tests/fixtures/expectation_stylish.txt'
EXPECTATION_PLAIN = 'tests/fixtures/expectation_plain.txt'
EXPECTATION_JSON = 'tests/fixtures/expectation_json.txt'


def test_wrong_file_gendiff():
    with pytest.raises(TypeError) as err:
        generate_diff(FILEPATH_WRONG, FILEPATH_WRONG)

    assert str(err.value) == 'Wrong extension!'


def test_wrong_format_gendiff():
    with pytest.raises(TypeError) as err:
        generate_diff(FILEPATH_JSON1_2, FILEPATH_JSON2_2, 'unstylish')

    assert str(err. value) == 'Wrong format!'


def test_default_format():
    assert (generate_diff(FILEPATH_JSON1,
                          FILEPATH_JSON2) == generate_diff(
            FILEPATH_JSON1, FILEPATH_JSON2, 'stylish'))


@pytest.mark.parametrize('first_file, second_file, format, expected', [
    (FILEPATH_JSON1_2, FILEPATH_JSON2_2,
     'stylish', open(EXPECTATION_STYLISH, 'r').read()),
    (FILEPATH_JSON1_2, FILEPATH_JSON2_2,
     'plain', open(EXPECTATION_PLAIN, 'r').read()),
    (FILEPATH_JSON1_2, FILEPATH_JSON2_2,
     'json', open(EXPECTATION_JSON, 'r').read()),
    (FILEPATH_YAML1_2, FILEPATH_YAML2_2,
     'stylish', open(EXPECTATION_STYLISH, 'r').read()),
    (FILEPATH_YAML1_2, FILEPATH_YAML2_2,
     'plain', open(EXPECTATION_PLAIN, 'r').read()),
    (FILEPATH_YAML1_2, FILEPATH_YAML2_2,
     'json', open(EXPECTATION_JSON, 'r').read()), ])
def test_generate_diff(first_file, second_file, format, expected):
    assert generate_diff(first_file, second_file, format) == expected

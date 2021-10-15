from gendiff.generate_difference import generate_diff, load_file_by_extension

FILEPATH_JSON1 = 'tests/fixtures/file1.json'
FILEPATH_JSON2 = 'tests/fixtures/file2.json'
FILEPATH_YAML = 'tests/fixtures/file2.yaml'


def test_json_file_opening():
    expectation = {"host": "hexlet.io", "timeout": 50,
                   "proxy": "123.234.53.22", "follow": False}
    assert load_file_by_extension(FILEPATH_JSON1) == expectation


def test_yaml_file_opening():
    expectation = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    assert load_file_by_extension(FILEPATH_YAML) == expectation


def test_default_format():
    assert (generate_diff(FILEPATH_JSON1,
                          FILEPATH_JSON2) == generate_diff(
            FILEPATH_JSON1, FILEPATH_JSON2, 'stylish'))

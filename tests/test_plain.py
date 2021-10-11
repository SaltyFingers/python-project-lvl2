from gendiff.formaters.plain_formater import format_value
import pytest
from gendiff.generate_difference import generate_diff


@pytest.fixture
def stylish_json_file_path1():
    return 'tests/fixtures/file1_2.json'


@pytest.fixture
def stylish_json_file_path2():
    return 'tests/fixtures/file2_2.json'


def test_plain_json(stylish_json_file_path1,
                    stylish_json_file_path2):
    expectation = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    assert generate_diff(stylish_json_file_path1,
                         stylish_json_file_path2, 'plain') == expectation


@pytest.fixture
def stylish_yaml_file_path1():
    return 'tests/fixtures/file1_2.yaml'


@pytest.fixture
def stylish_yaml_file_path2():
    return 'tests/fixtures/file2_2.yaml'


def test_plain_yaml(stylish_yaml_file_path1,
                    stylish_yaml_file_path2):
    expectation = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    assert generate_diff(stylish_yaml_file_path1,
                         stylish_yaml_file_path2, 'plain') == expectation


def test_decoding_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value({'a': 'b'}) == '[complex value]'
    assert format_value(300) == 300

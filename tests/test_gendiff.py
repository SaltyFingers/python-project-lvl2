# import pytest
# from gendiff.generate_difference import load_file_by_type


# @pytest.fixture
# def json_file_path():
#     return 'tests/fixtures/file1_2.json'


# @pytest.fixture
# def yaml_file_path():
#     return 'tests/fixtures/file2_2.yaml'

# def test_json_file_opening(json_file_path):
#     expectation = """{
#   "common": {
#     "setting1": "Value 1",
#     "setting2": 200,
#     "setting3": True,
#     "setting6": {
#       "key": "value",
#       "doge": {
#         "wow": ""
#       }
#     }
#   },
#   "group1": {
#     "baz": "bas",
#     "foo": "bar",
#     "nest": {
#       "key": "value"
#     }
#   },
#   "group2": {
#     "abc": 12345,
#     "deep": {
#       "id": 45
#     }
#   }
# }"""
#     assert str(load_file_by_type(json_file_path)) == expectation


# def test_yaml_file_opening(yaml_file_path):
#     expectation = """{
#   "common": {
#     "follow": False,
#     "setting1": "Value 1",
#     "setting3": None,
#     "setting4": "blah blah",
#     "setting5": {
#       "key5": "value5"
#     },
#     "setting6": {
#       "key": "value",
#       "ops": "vops",
#       "doge": {
#         "wow": "so much"
#       }
#     }
#   },
#   "group1": {
#     "foo": "bar",
#     "baz": "bars",
#     "nest": "str"
#   },
#   "group3": {
#     "deep": {
#       "id": {
#         "number": 45
#       }
#     },
#     "fee": 100500
#   }
# }"""
#     assert str(load_file_by_type(yaml_file_path)) == expectation

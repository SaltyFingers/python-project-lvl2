from gendiff.formaters.stylish_formater import (
    format_value, format_nested_object)


def test_format_value():
    assert format_value(False) == 'false'
    assert format_value(None) == 'null'


def test_format_nested_object():
    nested_object = {'deep': {'id': {'number': 45}}, 'fee': 100500}
    expectation = """{
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }"""
    assert format_nested_object(nested_object, 1) == expectation

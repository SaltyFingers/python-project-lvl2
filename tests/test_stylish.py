from gendiff.formaters.stylish_formater import (
    format_value, get_formated_dictionary)

nested_object = {'deep': {'id': {'number': 45}}, 'fee': 100500}


def test_format_value():
    assert format_value(False) == 'false'
    assert format_value(None) == 'null'
    assert format_value(nested_object) == get_formated_dictionary(nested_object, 1)


def test_get_formated_dictionary():
    expectation_nested = """{
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }"""
    assert get_formated_dictionary(nested_object, 1) == expectation_nested

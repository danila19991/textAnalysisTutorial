from task1.solution import change_sub_strings
import pytest


def test_change_sub_string_type_error():
    with pytest.raises(TypeError):
        change_sub_strings('egg spam', 1, '8')


def test_change_sub_string_vale_error():
    with pytest.raises(ValueError):
        change_sub_strings('egg spam', 'aba', 'ada')

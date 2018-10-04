"""
This module provides tests for first task solution.
"""


import pytest
from task1.solution import change_sub_strings


def test_change_sub_string_type_error():
    """
    Test for checking if type error would be raised.
    """
    with pytest.raises(TypeError):
        change_sub_strings('121', 1, '8')


def test_change_sub_string_vale_error():
    """
    Test for checking if value error would be raised.
    """
    with pytest.raises(ValueError):
        change_sub_strings('egg spam', 'aba', 'ada')

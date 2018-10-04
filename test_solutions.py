"""
This modules tests solution functions.
"""


from task1.solution import solution1
import pytest


def test_solution1_not_str():
    """
    Test for checking raising type error.
    """
    with pytest.raises(TypeError):
        solution1(1)

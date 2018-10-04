import pytest
from task1.solution import solution1


def test_solution1_not_str():
    with pytest.raises(TypeError):
        solution1(1, 2)

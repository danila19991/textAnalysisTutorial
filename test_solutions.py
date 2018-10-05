import pytest
from task1.solution1 import solution1
from task2.solution2 import solution2


def test_solution1_not_str():
    with pytest.raises(TypeError):
        solution1(1, 2)
    with pytest.raises(TypeError):
        solution2(1, 2, 3)

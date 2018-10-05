import pytest
from task1.solution1 import solution1
from task2.solution2 import solution2


@pytest.fixture(scope="function", params=[(TypeError, "121"),
                                          (TypeError, [1989])],
                ids=["not list", "not string"])
def param_list_of_string_raise(request):
    return request.param


def test_solution1_not_str():
    with pytest.raises(TypeError):
        solution1(1, 2)
    with pytest.raises(TypeError):
        solution2(1, 2, 3)

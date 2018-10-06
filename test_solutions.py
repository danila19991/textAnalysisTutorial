import pytest
from task1.solution1 import solution1
from task2.solution2 import solution2


@pytest.fixture(scope="function", params=[(TypeError, "121"),
                                          (TypeError, [1989])],
                ids=["not list", "not string"])
def param_list_of_string_raise(request):
    return request.param


def is_equal_lists(list1, list2):
    """
    Function for checking if list1 and list2 equal.

    :param list1: list
        First list for checking.

    :param list2: list
        Second list for checking.

    :return:
        True if equal, False otherwise.
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError
    list1.sort()
    list2.sort()
    return list1 == list2


@pytest.fixture(scope="function", params=[(TypeError, "121", [7])],
                ids=["not list and not string"])
def params_equal_lists_raise(request):
    return request.param


def test_equal_lists_raise(params_equal_lists_raise):
    error, list1, list2 = params_equal_lists_raise
    with pytest.raises(error):
        is_equal_lists(list1, list2)


@pytest.fixture(scope="function",
                params=[(["1989"], ['1989'], True),
                        (['1989'], ['1990'], False),
                        (['1989', '1990'], ['1990', '1989'], True),
                        (['1989'], ['1990', '1989'], False),
                        ([], [], True),
                        (['1989', '1989'], ['1990'], False),
                        (['1989', '1990'], ['1989', '1990'], True),
                        (['1989', '1989'], ['1989', '1989'], True),
                        (['1989', '1990'], ['1989', '1990', '1989'], False)],
                ids=["same list one element", 'different element',
                     'different order', 'first smaller than second',
                     'empty lists', 'first bigger than second',
                     'same list many elements', 'same list with repetitions',
                     'equal after deleting repetitions'])
def params_equal_lists(request):
    return request.param


def test_solution1_not_str():
    with pytest.raises(TypeError):
        solution1(1, 2)
    with pytest.raises(TypeError):
        solution2(1, 2, 3)

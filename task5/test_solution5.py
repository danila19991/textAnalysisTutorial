import pytest
from test_solutions import param_list_of_string_raise, is_equal_lists
from task5.solution5 import get_all_collocation


def test_get_all_collocation_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        get_all_collocation(lines, '')


def test_get_all_collocation_raise_second_param():
    with pytest.raises(TypeError):
        get_all_collocation([], 7)


@pytest.fixture(scope="function",
                params=[(['года она слово годы доля году фильм'], 'год',
                         ['год она', 'год доля', 'год фильм']),
                        (['года она', 'слово годы доля', 'году фильм'], 'год',
                         ['год она', 'год доля', 'год фильм']),
                        (['года.'], 'год', []),
                        (['года —'], 'год', [])],
                ids=['one line', 'multiple lines', 'word ends with .',
                     'word with —'])
def param_get_all_collocation(request):
    return request.param


def test_get_all_collocation(param_get_all_collocation):
    line, word, result = param_get_all_collocation
    assert is_equal_lists(get_all_collocation(line, word), result)

import pytest
from task1.solution import change_sub_strings


def test_change_sub_string_type_error():
    with pytest.raises(TypeError):
        change_sub_strings('121', 1, '8')


def test_change_sub_string_vale_error():
    with pytest.raises(ValueError):
        change_sub_strings('egg spam', 'aba', 'ada')


def test_change_sub_string_correct_strings():
    assert change_sub_strings('snake anaconda snake', 'snake', 'python') == \
        'python anaconda python'


def test_change_sub_string_correct_integers():
    assert change_sub_strings('12812', '12', '949') == '9498949'

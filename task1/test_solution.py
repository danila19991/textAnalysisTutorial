import pytest
from task1.solution import change_sub_strings, change_sentences


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


def test_change_sentences_correct_match():
    assert change_sentences(['python anaconda']) == ['python anaconda']


def test_change_sentences_correct_empty():
    assert change_sentences(['swallow anaconda']) == []


def test_change_sentences_correct_uppercase():
    assert change_sentences(['pYtHoN aNAcOnDa']) == ['python anaconda']


def test_change_sentences_correct_uppercase_with_change():
    assert change_sentences(['SNakE aNAcOnDa']) == ['python anaconda']


def test_change_sentences_correct_with_change():
    assert change_sentences(['snake anaconda']) == ['python anaconda']


def test_change_sentences_correct_type_error_list():
    with pytest.raises(TypeError):
        change_sentences('python anaconda')


def test_change_sentences_correct_type_error_string():
    with pytest.raises(TypeError):
        change_sentences([7])


def test_change_sentences_correct_some_strings():
    assert change_sentences(['python anaconda', 'swallow', 'anaconda snake'])\
           == ['python anaconda', 'anaconda python']


def test_change_sentences_correct_with_change_pattern_as_sub_word():
    assert change_sentences(['snakes anaconda']) == ['pythons anaconda']

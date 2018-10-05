import pytest
from task1.solution1 import change_sub_strings, change_sentences


@pytest.fixture(scope="function", params=[(TypeError, "121", 1, "8"),
                                          (ValueError, "egg spam",
                                           "aba", "ada")],
                ids=["TypeError", "ValueError"])
def param_change_sub_string_raise(request):
    return request.param


def test_change_sub_string_raise(param_change_sub_string_raise):
    error, text, pattern, next_string = param_change_sub_string_raise
    with pytest.raises(error):
        change_sub_strings(text, pattern, next_string)


@pytest.fixture(scope="function",
                params=[('snake anaconda snake', 'snake',
                         'python', 'python anaconda python'),
                        ('12812', '12', '949', '9498949')],
                ids=["string", "integer"])
def param_change_sub_string(request):
    return request.param


def test_change_sub_string(param_change_sub_string):
    text, pattern, next_string, result = param_change_sub_string
    assert change_sub_strings(text, pattern, next_string) == result


@pytest.fixture(scope="function", params=[(TypeError, 'python anaconda'),
                                          (TypeError, [7])],
                ids=["not list", "not string"])
def param_change_sentences_raise(request):
    return request.param


def test_change_sentences_raise(param_change_sentences_raise):
    error, text = param_change_sentences_raise
    with pytest.raises(error):
        change_sentences(text)


@pytest.fixture(scope="function",
                params=[(['python anaconda'], ['python anaconda']),
                        (['swallow anaconda'], []),
                        (['pYtHoN aNAcOnDa'], ['python anaconda']),
                        (['SNakE aNAcOnDa'], ['python anaconda']),
                        (['snake anaconda'], ['python anaconda']),
                        (['python anaconda', 'swallow', 'anaconda snake'],
                         ['python anaconda', 'anaconda python']),
                        (['snakes anaconda'], ['pythons anaconda'])],
                ids=["no changes", "not match", "upper case",
                     "upper case with change", "change", "some lines",
                     "sub word for change"])
def param_change_sentences(request):
    return request.param


def test_change_sentences(param_change_sentences):
    text, answer = param_change_sentences
    assert change_sentences(text) == answer

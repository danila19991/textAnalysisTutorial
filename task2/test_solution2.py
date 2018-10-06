import pytest
from task2.solution2 import get_all_years, filter_same_tokens, find_all_tokens
from test_solutions import param_list_of_string_raise, is_equal_lists, \
    params_equal_lists


def test_get_all_years_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        get_all_years(lines)


@pytest.fixture(scope="function",
                params=[(['1989'], ['1989']),
                        (['egg spam'], []),
                        ([], []),
                        (['1989', '2014'], ['1989', '2014']),
                        (['1989 2014'], ['1989', '2014']),
                        (['text 1989 another text 2014 more text'],
                         ['1989', '2014']),
                        (['1989 text', 'text 2001'], ['1989', '2001']),
                        (['1989 2651tty'], ['1989', '2651']),
                        (['1989', 'text', '1756 year'], ['1756', '1989']),
                        (['1989', '2018', '1753'], ['1753', '1989', '2018']),
                        (['2018 1989 1945'], ['1945', '1989', '2018']),
                        (['1989', '1989'], ['1989'])],
                ids=["already answer", "no years", "empty",
                     "already answer list", "one string", "big test",
                     "many lines with text", "year as sub word",
                     "string with no year", "not sorted list",
                     "not sorted in one line", "with repetitions"])
def param_get_all_years(request):
    return request.param


def test_get_all_years(param_get_all_years):
    lines, answer = param_get_all_years
    assert get_all_years(lines) == answer


def test_equal_lists(params_equal_lists):
    list1, list2, result = params_equal_lists
    assert is_equal_lists(list1, list2) == result


@pytest.fixture(scope="function",
                params=[(['egg', 'spam', 'egg'], ['egg', 'spam']),
                        (['egg', 'egg', 'egg'], ['egg']),
                        (["egg's", 'egg', 'egg'], ["egg's", 'egg']),
                        (['egg', 'spam'], ['egg', 'spam'])],
                ids=['one repetition', 'all elements are repetitions',
                     'repetitions with "\'s"', 'already answer'])
def param_filter_same_tokens(request):
    return request.param


def test_filter_same_tokens_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        filter_same_tokens(lines)


def test_filter_same_tokens(param_filter_same_tokens):
    tokens, answer = param_filter_same_tokens
    assert is_equal_lists(filter_same_tokens(tokens), answer)


@pytest.fixture(scope="function",
                params=[(['egg', 'spam', 'egg'], ['egg', 'spam', 'egg']),
                        (['egg egg egg'], ['egg', 'egg', 'egg']),
                        (["egg's", 'egg', 'egg'], ["egg's", 'egg', 'egg']),
                        (['egg', 'spam'], ['egg', 'spam']),
                        (['“ogre”.', '2000'], ['ogre', '2000']),
                        (['“ogre”. (III)', '2000 ~III  ', 'mission—this'],
                         ['ogre', '2000', 'iii', 'iii', 'mission—this']),
                        (["“17'th”.", '2000'], ["17'th", '2000']),
                        (['EgG SpAm'], ['egg', 'spam'])],
                ids=['already answer with repetitions',
                     'one line with repetitions', 'repetitions with "\'s"',
                     'already answer', 'special symbols', 'word with "—"',
                     'number with "\'th"', 'different cases'])
def param_find_all_tokens(request):
    return request.param


def test_find_all_tokens_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        find_all_tokens(lines)


def test_find_all_tokens(param_find_all_tokens):
    lines, tokens = param_find_all_tokens
    assert is_equal_lists(find_all_tokens(lines), tokens)

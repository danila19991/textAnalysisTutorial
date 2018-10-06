import pytest
from task4.solution4 import find_all_words, find_most_popular, \
    get_all_words_from_articles
from test_solutions import param_list_of_string_raise, is_equal_lists
from models.article import Article


def test_find_all_words_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        find_all_words(lines)


@pytest.fixture(scope="function",
                params=[(['яйцо', 'омлет', 'яйцо'], ['яйцо', 'омлет', 'яйцо']),
                        (['яйцо яйцо яйцо'], ['яйцо', 'яйцо', 'яйцо']),
                        (["яйца", 'яйцо', 'яйцо'], ["яйцо", 'яйцо', 'яйцо']),
                        (['яйцо', 'омлет'], ['яйцо', 'омлет']),
                        (['“руда”.', '2000'], ['руда', '2000']),
                        (['“руда”. (III)', '2000 ~III  ', 'красно—черный'],
                         ['руда', 'красный', 'чёрный', '2000', 'iii', 'iii']),
                        (["“17-й”.", '2000'], ['17-ть', '2000']),
                        (['ЯйЦо ОмлЕт'], ['яйцо', 'омлет']),
                        (['Во Владивостоке проходит 16-й международный ' \
                          'кинофестиваль «Меридианы Тихого»'],
                         ['в', 'владивосток', 'проходить', 'международный',
                          'кинофестиваль', 'меридиан', 'тихий', '16-ть']),
                        (['жёстко'], ['жёстко']),
                        (['44-летний'], ['44-летний'])],
                ids=['already answer with repetitions',
                     'one line with repetitions', 'repetitions with normalise',
                     'already answer', 'numbers', 'word with "—"',
                     'number with "-й"', 'different cases', 'real text',
                     'with "Ё"', 'word with -'])
def param_find_all_words(request):
    return request.param


def test_find_all_words(param_find_all_words):
    param, result = param_find_all_words
    assert is_equal_lists(find_all_words(param), result)


def test_find_most_popular_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        find_most_popular(lines, [], 7)
    with pytest.raises(error):
        find_most_popular([], lines, 7)


def test_find_most_popular_raise_not_int():
    with pytest.raises(TypeError):
        find_most_popular([], [], '7')


@pytest.fixture(scope="function",
                params=[(['яйцо', 'омлет', 'яйцо'], [], 1, ['яйцо']),
                        (['яйцо', 'яйцо', 'яйцо'], [], 1, ['яйцо']),
                        (["яйцо", 'яйцо', 'яйцо'], ['яйцо'], 1, []),
                        (['яйцо', 'омлет', 'яйцо'], ['яйцо'], 1, ['омлет']),
                        (['яйцо', 'омлет'], [], 3, ['яйцо', 'омлет']),
                        (['в', 'локоть'], ['в'], 1, ['локоть']),
                        (['слово', 'время', 'слово', 'задача', 'слово',
                          'время'], [], 2, ['слово', 'время'])],
                ids=['words 2:1', 'one word', 'all words forbidden',
                     'words 2:1 and 1 forbidden', 'need more than have',
                     'erased russian word', 'need to sort big test'])
def param_find_most_popular(request):
    return request.param


def test_find_most_popular(param_find_most_popular):
    words, forbidden, n, result = param_find_most_popular
    assert is_equal_lists(find_most_popular(words, forbidden, n), result)


def test_get_all_words_from_articles_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        get_all_words_from_articles(lines)


@pytest.fixture(scope="function",
                params=[([('Сложно', 'Ульяна', '23.09.2018, 10:15', 'текст'),
                          ('Просто', 'Вася', '23.09.2018, 10:16', 'качество')],
                         ['сложно', 'просто', 'текст', 'качество'])],
                ids=['two test article'])
def param_get_all_words_from_articles(request):
    return request.param


def test_get_all_words_from_articles(param_get_all_words_from_articles):
    articles_param, result = param_get_all_words_from_articles

    articles = []
    for param in articles_param:
        name, author, date, text = param
        articles.append(Article(name, author, date, text))

    assert is_equal_lists(get_all_words_from_articles(articles), result)

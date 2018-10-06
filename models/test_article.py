import pytest
from time import strptime
from models.article import Article, parse_articles_from_lines
from test_solutions import param_list_of_string_raise


@pytest.fixture(scope="function",
                params=[('name', 'author', '23.09.2018, 10:15', 'text',
                         'name\nАвтор: author\nДата: 23.09.2018, 10:15\n' \
                         'text\n-----------')],
                ids=['test article'])
def param_article_model_example(request):
    return request.param


def test_article_constructor_and_to_string(param_article_model_example):
    name, author, date, text, string = param_article_model_example

    article = Article(name, author, date, text)

    assert article.name == name
    assert article.author == author
    assert article.date == strptime(date, '%d.%m.%Y, %H:%M')
    assert article.text == text
    assert str(article) == string
    assert article.all_text == [name, text]


@pytest.fixture(scope="function",
                params=[('23.09.2018, 10:15', '23.09.2018, 10:15', False),
                        ('23.10.2018, 11:15', '23.09.2018, 10:15', False),
                        ('23.09.2018, 10:15', '23.10.2018, 10:15', True),
                        ('23.09.2018, 10:15', '24.09.2018, 10:15', True),
                        ('23.09.2018, 10:15', '23.09.2018, 10:16', True),
                        ('23.09.2018, 10:15', '23.09.1217, 10:15', False)],
                ids=['equal', 'greater month', 'less month', 'less day',
                     'less minute', 'greater year'])
def param_article_lt(request):
    return request.param


def test_article_lt(param_article_lt):
    date1, date2, result = param_article_lt
    article_left = Article('name', 'author', date1, 'text')
    article_rieght = Article('name', 'author', date2, 'text')
    assert (article_left < article_rieght) == result


@pytest.fixture(scope="function",
                params=[('name', 'author', '23.09.2018, 10:15', 'text',
                         'name', 'author', '23.09.2018, 10:15', 'text', True),
                        ('name', 'author', '23.09.2018, 10:15', 'text',
                         'name', 'author', '23.09.2018, 10:16', 'text',
                         False)],
                ids=['equal', 'not equal'])
def param_article_eq(request):
    return request.param


def test_article_eq(param_article_eq):
    name1, author1, date1, text1, name2, author2, date2, text2, result =\
        param_article_eq
    article_left = Article(name1, author1, date1, text1)
    article_rieght = Article(name2, author2, date2, text2)
    assert (article_left == article_rieght) == result


def test_parse_articles_from_lines_one_article(param_article_model_example):
    name, author, date, text, string = param_article_model_example
    article = Article(name, author, date, text)
    assert parse_articles_from_lines(string.split('\n')) == [article]


def test_parse_articles_from_lines_raise(param_list_of_string_raise):
    error, lines = param_list_of_string_raise
    with pytest.raises(error):
        parse_articles_from_lines(lines)


@pytest.fixture(scope="function",
                params=[([('name1', 'author1', '23.09.2018, 10:15', 'text1'),
                          ('name2', 'author2', '23.09.2018, 10:16', 'text2')],
                         'name1\nАвтор: author1\nДата: 23.09.2018, 10:15\n' \
                         'text1\n-----------\n________________\nname2\n'\
                         'Автор: author2\nДата: 23.09.2018, 10:16\n' \
                         'text2\n-----------')],
                ids=['test article'])
def param_parse_articles_from_lines_many_articles(request):
    return request.param


def test_parse_articles_from_lines_many_articles(
        param_parse_articles_from_lines_many_articles):
    article_param, string = param_parse_articles_from_lines_many_articles
    articles = []
    for param in article_param:
        name, author, date, text = param
        articles.append(Article(name, author, date, text))
    assert parse_articles_from_lines(string.split('\n')) == articles

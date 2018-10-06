import pymorphy2
import re
import operator
from models.article import get_article_list_from_file, Article


class normalizer:
    """
    Class for not reinitialising morph analyser.
    """
    _morph = pymorphy2.MorphAnalyzer()

    @classmethod
    def normalise(cls, word):
        """
        Function for normalising word.

        :param word: str
            Word for normalising.

        :return:
            First version of normalised word.
        """
        return cls._morph.parse(word)[0].normal_form


def find_all_words(lines):
    """
    Function for finding all normalised words in lines.

    :param lines: list of string
        Lines for searching

    :return:
        List of all words in
    """
    if not isinstance(lines, list):
        raise TypeError

    matcher = re.compile(r"[-ёа-яЁА-Я0-9a-zA-Z]+")

    result = []

    for line in lines:
        if not isinstance(line, str):
            raise TypeError
        for word in matcher.findall(line):
            if word != '-й':
                result.append(normalizer.normalise(word))

    return result


def find_most_popular(words, forbidden_words, n):
    """
    Function for finding n most popular words

    :param words: list of string
        Words for analysing.

    :param n: int
        Number of elements for searching.
        
    :param forbidden_words: list of str
        List of words which is forbidden for searching.

    :return:
        List of most popular words, with length less or equal to n.
    """
    if not isinstance(words, list) or not isinstance(n, int) or \
            not isinstance(forbidden_words, list):
        raise TypeError

    for word in forbidden_words:
        if not isinstance(word, str):
            raise TypeError

    word_dictionary = {}

    for word in words:
        if not isinstance(word, str):
            raise TypeError
        if word in forbidden_words:
            continue
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    sorted_words = \
        sorted(word_dictionary.items(), key=operator.itemgetter(1))[::-1]

    result = []

    for i in range(min(n, len(sorted_words))):
        result.append(sorted_words[i][0])

    return result


def get_all_words_from_articles(articles):
    """
    Function for getting all words from list of articles.

    :param articles: list of articles
        List of articles for processing.

    :return:
        List of words from articles.
    """
    if not isinstance(articles, list):
        raise TypeError

    words = []

    for article in articles:
        if not isinstance(article, Article):
            raise TypeError
        words += find_all_words(article.all_text)

    return words


def solution4(source_file, result_file, ignore_list_file, n):
    """
    Function for parsing all articles from source_file, find all words and
    writing n most popular to result_file.

    :param source_file: str
        File name with articles.

    :param result_file: str
        File name for writing articles.

    :param ignore_list_file: str
        File with list of forbidden words.

    :param n: int
        Number of most popular words for searching.
    """
    if not isinstance(source_file, str) or \
            not isinstance(result_file, str) or not isinstance(n, int) or\
            not isinstance(ignore_list_file, str):
        raise TypeError

    try:
        articles = get_article_list_from_file(source_file)

        forbidden = []

        with open(ignore_list_file, 'rb') as f_in:
            for word in f_in.readlines():
                word = word.decode()
                if word[-2:] == '\r\n':
                    word = word[:-2]
                forbidden.append(word)

        words = get_all_words_from_articles(articles)

        result = find_most_popular(words, forbidden, n)

        print(result)

        with open(result_file, 'wb') as f_out:
            f_out.write('\n'.join(result).encode())
    except FileNotFoundError:
        print("can't open file in solution 4")

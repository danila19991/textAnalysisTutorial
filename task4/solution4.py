import pymorphy2
import re
import operator
from models.article import get_article_list_from_file, \
    get_all_lines_from_articles


class Normalizer:
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
                result.append(Normalizer.normalise(word))

    return result


def get_inclusion_number(custom_list):
    """
    Function for getting dict with number of inclusion of element in list.

    :param custom_list: list
        List for analysing

    :return:
        Dict with number of inclusions for every element.
    """
    if not isinstance(custom_list, list):
        raise TypeError

    result = {}

    for elem in custom_list:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1

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

    for word in words:
        if not isinstance(word, str):
            raise TypeError

    word_dictionary = get_inclusion_number(words)

    sorted_words = \
        sorted(word_dictionary.items(), key=operator.itemgetter(1))[::-1]

    result = []

    for word in sorted_words:
        if word[0] in forbidden_words:
            continue
        result.append(word[0])
        if len(result) >= n:
            break

    return result


def read_all_words_from_file(source_file):
    """
    Function for read all words from source file.

    :param source_file: str
        File with words.

    :return:
        List of words.
    """
    if not isinstance(source_file, str):
        raise TypeError

    with open(source_file, 'rb') as f_in:
        words = [word.decode().strip() for word in f_in]

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
        result = find_most_popular(
            find_all_words(get_all_lines_from_articles(
                get_article_list_from_file(source_file))),
            read_all_words_from_file(ignore_list_file), n)

        with open(result_file, 'wb') as f_out:
            f_out.write('\n'.join(result).encode())
    except FileNotFoundError:
        print("can't open file in solution 4")

import operator
from yargy import rule, not_, Parser, and_
from yargy.predicates import normalized, type
from task4.solution4 import get_inclusion_number, find_most_popular, \
    find_all_words, read_all_words_from_file, Normalizer
from models.article import get_article_list_from_file, \
    get_all_lines_from_articles


def get_all_collocation(lines, word):
    """
    Function for finding all collocations of word and any word after it.

    :param lines: list of string
        Lines for processing.

    :param word: str
        Word for searching.

    :return:
        List of all valid collocations.
    """
    if not isinstance(lines, list) or not isinstance(word, str):
        raise TypeError

    gr = rule(normalized(word), and_(not_(type('PUNCT')),
                                      not_(type('OTHER'))))

    result_list = []

    for line in lines:
        if not isinstance(line, str):
            raise TypeError
        for match in Parser(gr).findall(line):
            result_list.append(
                ' '.join([Normalizer.normalise(token.value)
                          for token in match.tokens]))

    return result_list


def solution5(source_file, result_file, ignore_list_file, n):
    """
    Function for finding pairs with most popular words.

    :param source_file: str
        File with articles.

    :param result_file: str
        File for saving answers.

    :param ignore_list_file: str
        File with list of forbidden words.

    :param n: int
        Number of most popular words for searching.
    """
    if not isinstance(source_file, str) or not isinstance(result_file, str) \
            or not isinstance(n, int) or not isinstance(ignore_list_file, str):
        raise TypeError

    try:
        lines = get_all_lines_from_articles(
            get_article_list_from_file(source_file))

        popular = find_most_popular(find_all_words(lines),
            read_all_words_from_file(ignore_list_file), n)

        collocation_list = []

        for word in popular:
            collocation_list += get_all_collocation(lines, word)

        sorted_collocations = \
            sorted(get_inclusion_number(collocation_list).items(),
                   key=operator.itemgetter(1))[::-1]

        with open(result_file, 'wb') as f_out:
            for collocation, number in sorted_collocations:
                f_out.write((collocation + ': ' + str(number) + '\n').encode())
    except FileNotFoundError:
        print("can't open file in solution 5")


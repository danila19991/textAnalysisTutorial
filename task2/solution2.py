import re


def get_all_years(lines):
    """
    Function for finding list of all years in text and sort it.

    :param lines: list with str
        List of sentences.

    :return:
        Sorted list of years.
    """
    if not isinstance(lines, list):
        raise TypeError

    for line in lines:
        if not isinstance(line, str):
            raise TypeError

    matcher = re.compile(r"[\d]{4}")

    years = []

    for line in lines:
        years += matcher.findall(line)

    years = filter_same_tokens(years)

    years.sort()

    return years


def filter_same_tokens(tokens):
    """
    Function for filtering repetitions in tokens.

    :param tokens: list with str
        List of tokens for filtering.

    :return:
        Filtered list of tokens without repetitions.
    """
    if not isinstance(tokens, list):
        raise TypeError

    for token in tokens:
        if not isinstance(token, str):
            raise TypeError

    tmp_set = set(tokens)

    return [token for token in tmp_set]


def find_all_tokens(lines):
    """
    Function for finding list of all tokens in text.

    :param lines: list with str
        List of sentences.

    :return:
        List of tokens.
    """
    if not isinstance(lines, list):
        raise TypeError

    matcher = re.compile(r"([—a-zA-Z]+('s)?|[0-9]+('th)?)")

    tokens = []

    for line in lines:
        if not isinstance(line, str):
            raise TypeError
        for pairs in matcher.findall(line):
            tokens.append(pairs[0].lower())

    return tokens


def solution2(source_file, token_file, years_file):
    """
    Function for reading sentences from source_file, making tokenization and
    writing it ot token_file, also find all 4-digits number sort it and write
    to years_file.

    :param source_file: str
        File name with sentences for processing.

    :param token_file: str
        File name for writing tokens.

    :param years_file:
        File name for writing years.
    """
    if not isinstance(source_file, str) or not isinstance(token_file, str) or\
            not isinstance(years_file, str):
        raise TypeError

    try:
        with open(source_file, 'r') as f_in:
            lines = f_in.readlines()
            with open(token_file, 'w') as f_out:
                f_out.writelines(
                    '\n'.join(filter_same_tokens(find_all_tokens(lines))))
            with open(years_file, 'w') as f_out:
                f_out.writelines('\n'.join((get_all_years(lines))))
    except FileNotFoundError:
        print("can't open file in second solution")

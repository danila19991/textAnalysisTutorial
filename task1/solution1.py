"""
This module provide solution for first task.
"""


def change_sub_strings(text, pattern, new_string):
    """
    Function for changing all entrance of pattern to new_string.

    :param text: str
        String for changing.

    :param pattern: str
        String which should be removed. Any suffix of this string shouldn't be
        equal to prefix of same length.

    :param new_string: str
        String which should be added.

    :return:
        String with changed pattern to new_string.
    """
    if not isinstance(text, str) or not isinstance(pattern, str) or \
            not isinstance(new_string, str):
        assert TypeError

    for i in range(1, len(pattern)):
        if pattern[:i] == pattern[-i:]:
            raise ValueError

    return new_string.join(text.split(pattern))


def change_sentences(lines):
    """
    Function for set all letters to lower case, changing all 'snake' to
    'python' and filtering all sentence where no 'python' or 'anaconda'

    :param lines: list with str
        List of sentences for processing.

    :return:
        List of sentences with 'python' and 'anaconda'.
    """
    if not isinstance(lines, list):
        raise TypeError

    result = []

    for line in lines:
        if not isinstance(line, str):
            raise TypeError

        line = change_sub_strings(line.lower(), 'snake', 'python')
        if 'python' in line and 'anaconda' in line:
            result.append(line)

    return result


def solution1(input_file_name, output_file_name):
    """
    Function for solving first task.

    :param input_file_name: str
        Name of file for processing.

    :param output_file_name: str
        Name of file for writing result.

    :return:
        Text with changed substrings.
    """
    if not isinstance(input_file_name, str) or \
            not isinstance(output_file_name, str):
        raise TypeError

    try:
        with open(input_file_name, 'r') as f_in:
            with open(output_file_name, 'w') as f_out:
                f_out.writelines(change_sentences(f_in.readlines()))
    except FileNotFoundError:
        print("can't open file")

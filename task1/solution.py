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
        with open(input_file_name, 'r') as fin:
            with open(output_file_name, 'w') as fout:
                for line in fin.readlines():
                    line = change_sub_strings(line.lower(), 'snake', 'python')
                    if 'python' in line and 'anaconda' in line:
                        fout.writelines(line)
    except FileNotFoundError:
        print("can't open file")

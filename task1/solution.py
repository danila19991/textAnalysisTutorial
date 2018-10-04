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
    if isinstance(text, str) and isinstance(pattern, str) and \
            isinstance(new_string, str):
        assert TypeError

    for i in range(1, len(pattern)):
        if pattern[:i] == pattern[-i:]:
            raise ValueError

    return text

from time import strptime, strftime


class Article:
    """
    Class for storing information about articles
    """

    time_pattern = '%d.%m.%Y, %H:%M'

    def __init__(self, name, author, date, text):
        """
        Default constructor.

        :param name: str
            Name of this article.

        :param author: str
            Author of this article

        :param date: str
            Date, when article was wrote.

        :param text: str
            Text of article.
        """
        if not isinstance(name, str) or not isinstance(author, str) or \
                not isinstance(date, str) or not isinstance(text, str):
            raise TypeError
        self._name = name
        self._date = strptime(date, self.time_pattern)
        self._text = text
        self._author = author

    def __lt__(self, other):
        """
        Less function for class.

        :param other: Article
            Other instance of Article class.

        :return:
            True if this article was earlier than other.
        """
        if not isinstance(other, Article):
            raise TypeError
        return self.date < other.date

    def __str__(self):
        """
        Function for making string from this article.

        :return:
            String presentation of this class.
        """
        return f'{self.name}\nАвтор: {self.author}\n'\
               f'Дата: {strftime(self.time_pattern, self.date)}\n{self.text}'\
               '\n-----------'

    def __eq__(self, other):
        """
        Function for checking if two articles equal.

        :param other: Article
            Other instance of article for checking.

        :return:
            True if self and other is equal.
        """
        if not isinstance(other, Article):
            raise TypeError
        return self.author == other.author and self.text == other.text and \
                self.name == other.name and self.date == other.date

    @property
    def name(self):
        """
        Getter for name field.

        :return:
            Name of article.
        """
        return self._name

    @property
    def date(self):
        """
        Getter for date field.

        :return:
            Date of article.
        """
        return self._date

    @property
    def text(self):
        """
        Getter for text of article.

        :return:
            Text of article.
        """
        return self._text

    @property
    def author(self):
        """
        Getter for author of article.

        :return:
            Author of article.
        """
        return self._author


def parse_articles_from_lines(lines):
    """
    Function for creating list of Articles from lines, read from file.

    :param lines: list of string
        List of strings for parsing.

    :return:
        List of Articles.
    """
    if not isinstance(lines, list):
        raise TypeError

    state = 0
    name = ''
    author = ''
    data = ''
    text = ''
    result = []

    for line in lines:
        if not isinstance(line, str):
            raise TypeError
        if line[-2:] == '\r\n':
            line = line[:-2]
        if line == '':
            continue
        if state == 0:
            name = line
            state = 1
            continue
        if state == 1:
            tmp = line.split('Автор: ')
            author = tmp[-1]
            state = 2
            continue
        if state == 2:
            data = line.split('Дата: ')[-1]
            state = 3
            continue
        if state == 3:
            text = line
            state = 4
            continue
        if state == 4:
            if line == '-----------':
                result.append(Article(name, author, data, text))
                state = 5
                continue
            text += '\n' + line
            continue
        if state == 5 and line == '________________':
            state = 0
            continue

    return result
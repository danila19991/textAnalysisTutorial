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

    @property
    def all_text(self):
        """
        Getter for all text and name in article.

        :return:
            List with name and text
        """
        return [self._name, self._text]


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
        line = line.strip()
        if not line:
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


def get_article_list_from_file(file_name):
    """
    Function for parsing file with articles.

    :param file_name: str
        Name of file for parsing.

    :return:
        List of articles.
    """

    if not isinstance(file_name, str):
        raise TypeError

    with open(file_name, 'rb') as f_in:
        return parse_articles_from_lines([line.decode() for line in f_in])


def save_article_list_to_file(articles, file_name):
    """
    Function for writing list of articles to file.

    :param articles: list of articles
        List of articles for writing

    :param file_name: str
        Name of file for saving.
    """

    if not isinstance(file_name, str) or not isinstance(articles, list):
        raise TypeError

    for article in articles:
        if not isinstance(article, Article):
            raise TypeError

    with open(file_name, 'wb') as f_out:
        text = '\n________________\n'.join([str(article)
                                            for article in articles])
        f_out.write(text.encode())


def get_all_lines_from_articles(articles):
    """
    Function for getting list of lines names and text of articles in list.

    :param articles: list of articles
        Articles for parsing.

    :return:
        List of text lines in articles.
    """
    if not isinstance(articles, list):
        raise TypeError

    result = []

    for article in articles:
        if not isinstance(article, Article):
            raise TypeError
        result.append(article.name)
        result += article.text.split('\n')

    return result

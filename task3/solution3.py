from models.article import Article, parse_articles_from_lines


def solution3(source_file, result_file):
    """
    Function for parsing all articles from source_file and writing all
    articles sorted by date to result_file.

    :param source_file: str
        File name with articles.

    :param result_file: str
        File name for writing articles.
    """
    if not isinstance(source_file, str) or \
            not isinstance(result_file, str):
        raise TypeError

    try:
        with open(source_file, 'rb') as f_in:
            with open(result_file, 'wb') as f_out:
                lines = []
                for line in f_in.readlines():
                    lines.append(line.decode())

                articles = parse_articles_from_lines(lines)
                articles.sort()
                articles = list(map(str, articles))

                text = '\n________________\n'.join(articles)

                f_out.write(text.encode())
    except FileNotFoundError:
        print("can't open file in third solution")

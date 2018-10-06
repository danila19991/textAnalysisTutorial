from models.article import get_article_list_from_file, \
    save_article_list_to_file


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
        articles = get_article_list_from_file(source_file)
        articles.sort()
        save_article_list_to_file(articles, result_file)
    except FileNotFoundError:
        print("can't open file in third solution")

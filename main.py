

"""Fetch and print words

Usage:
    python main.py <filepath>
    ./main.py <filepath>
    from main import main
    main(<filepath)

"""

import sys


def fetch_words(filepath):
    """
    Fetch words from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: word list from given filepath
    :rtype: list[str]
    """
    with open(filepath, 'r') as file:
        return [word for line in file for word in line.split()]


def print_items(items):
    """
    Prints items from iterable
    :param items: any iterable collection of data
    :type items: iterable
    :return: none
    :rtype: none
    """
    for item in items:
        print(item)


def main(filepath):
    """
    Fetch words from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: None
    :rtype: None
    """
    words = fetch_words(filepath)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # Zero-index is module name

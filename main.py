import re


def plus(a, b):
    return a+b


def main():
    print(plus('hello ', 'world'))
    matcher = re.compile('snake')
    print(matcher.split('snake snake'))

if __name__ == "__main__":
    main()

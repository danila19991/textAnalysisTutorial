from task1.solution1 import solution1
from task2.solution2 import solution2, find_all_tokens


def main():
    #print(find_all_tokens(['mission—this']))
    solution1('anaconda.txt', 'result1.txt')
    solution2('anaconda.txt', 'result2.1.txt', 'result2.2.txt')


if __name__ == "__main__":
    main()

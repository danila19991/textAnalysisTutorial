from task1.solution1 import solution1
from task2.solution2 import solution2
from task3.solution3 import solution3
from task4.solution4 import solution4
from task5.solution5 import solution5


def main():
    solution1('anaconda.txt', 'result1.txt')
    solution2('anaconda.txt', 'result2.1.txt', 'result2.2.txt')
    solution3('News.txt', 'result3.txt')
    solution4('News.txt', 'result4.txt', 'forbidden.txt', 50)
    solution5('News.txt', 'result5.txt', 'forbidden.txt', 5)


if __name__ == "__main__":
    main()

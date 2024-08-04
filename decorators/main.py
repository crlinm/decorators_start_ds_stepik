import time
from functools import lru_cache, cache

import requests
import re

from benchmark import benchmark
from counter import counter
from logging_ import logging
from memo import memo


@counter
@logging
@benchmark
def word_count(word, url='https://www.gutenberg.org/files/2638/2638-0.txt'):
    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('\\W+', ' ', raw).lower()

    # считаем
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"


@counter
def say_hi():
    print('hi')


def main():
    print('First part: word_count \n')
    print(word_count('whole'), '\n')
    print(word_count('preceding'), '\n')
    # say_hi()
    # say_hi()
    # print(word_count('computer'))
    # print(word_count('insane'))
    # say_hi()


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


# @cache
# @lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


@memo
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n-2) + fib_memo(n-1)


def main_fibonacci():
    print('Second part: fibonacci algorithm \n')

    start_time = time.time()
    print("recursive Fibonacci algorithm:")
    fib(10)
    end_time = time.time()
    print(f"Время выполнения функции {fib.__name__}: {end_time - start_time}")

    start_time = time.time()
    print("\nrecursive Fibonacci algorithm using memoization:")
    fib_memo(10)
    end_time = time.time()
    print(f"Время выполнения функции {fib_memo.__name__}: {end_time - start_time}")
    print("cache: ", fib_memo.cache)


if __name__ == '__main__':
    main()
    main_fibonacci()


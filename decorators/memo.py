from benchmark import benchmark


def memo(func):
    """
    Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
    """
    cache = {}

    def fmemo(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    fmemo.cache = cache
    return fmemo


@benchmark
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

@benchmark
@memo
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n-2) + fib_memo(n-1)


def main4():
    fib(10)
    print()
    fib_memo(10)
    print(fib_memo.cache)


if __name__ == '__main__':
    main4()



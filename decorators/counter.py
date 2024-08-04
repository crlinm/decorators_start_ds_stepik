from functools import wraps


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    k = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        nonlocal k
        k += 1
        print(f"Функция {func.__name__} вызвана {k} раз")
        return res

    return wrapper

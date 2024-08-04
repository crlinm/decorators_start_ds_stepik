from functools import wraps


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызвана с параметрами:')
        print(args, kwargs)
        return res
    return wrapper

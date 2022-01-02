from math import factorial
from time import time, sleep

# decorator factory
def calc_time():
    def decorator(func):
        def inner(*args, **kwargs):
            begin = time()

            func(*args, **kwargs)

            end = time()
            print(
                f"Total time to execute the '{func.__name__}' was: {end - begin}s"
            )

        return inner

    return decorator


@calc_time()
def do_factorial(num: int):
    sleep(2)
    print(factorial(num))

    # do_factorial(10)


def hello_decorator(func):
    """
    Changing return values of a function with decorators
    """

    def inner1(*args, **kwargs):
        print("Hello before")

        result = func(*args, **kwargs)

        print("Hello after")
        return result

    return inner1


@hello_decorator
def do_sum(x: int, y: int):
    print(f"Sum of {x} and {y} is: {x + y}")


# do_sum(10, 15)


def multiply_10x(func):
    """
    Decorator chaining
    """

    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x * 10

    return inner


def multiply_5x(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x * 5

    return inner


@multiply_5x
@multiply_10x
def get_num():
    return 2


# print(get_num())


# Class decorator
def practice_decor():
    def decorator(cls):
        cls.username = "Rabbi"
        return cls

    return decorator


@practice_decor()
class User:
    username = "Sifatul"

    def __init__(self):
        pass


print(User().username)

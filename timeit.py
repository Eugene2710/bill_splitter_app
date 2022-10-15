from datetime import datetime
from typing import Callable, Any


# We created a function wrapper here;
# it takes in a function, and edits it to print out the time it took to run
def timeit(func: Callable[[...], Any]) -> Callable[[...], Any]:
    def timedfunc(*args, **kwargs):
        start: datetime = datetime.utcnow()
        result: Any = func(*args, **kwargs)
        end: datetime = datetime.utcnow()
        print(f"{func.__name__} took {(end - start).microseconds} microseconds")
        return result
    return timedfunc


@timeit
def valid_palindrome(input: str) -> bool:
    return input == input[::-1]


# "cheese" is a arg
valid_palindrome("cheese")
# (input, "cheese") is a kwarg
valid_palindrome(input="cheese")

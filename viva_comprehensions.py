from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1

def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    Based on parity (odd or even), return a list from the start and end arguments.


     https://docs.python.org/3/howto/enum.html

    :param start:
    :param stop:
    :param parity:
    :return:
    """

    output = [nums for nums in range (start,stop) if parity == 1 or 0]
    return output
    #pass



def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

        Based on strategy return a dictionary start and not including stop integers as key pairs with its result
        strategy 1 is squaring the int
        strategy 2 is getting the factorial

    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    output = { x: strategy(x) for x in range (start, stop) }
    return output


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    return a set that takes the lowercase letters in a string and turns them into uppercase. Not sure what the last
    one is doing. it takes all uppercase string and returns an empty set?
    found this example in the book.
    set comprehension.

    :param val_in:
    :return:
    """
    output = {val_in.upper() for val_in in val_in if val_in.islower()}
    return output


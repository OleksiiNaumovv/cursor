"""
This is a list of functions that should be completed.
"""

from string import ascii_lowercase
from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
      If @first and @second has same value should return True
      In another case should return False
      """
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
        If @first and @second has same type should return True
        In another case should return False
        """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
        If @first and @second has same type should return True
        In another case should return False
        """
    return first is second


def multiple_ints(first_value: int, second_value: int) -> int:
    """
       Should calculate product of all args.
       if first_value or second_value is not int should raise ValueError

       Raises:
           ValueError

       Params:
           first_value: value for multiply
           second_value
       Returns:
           Product of elements
       """
    if type(first_value) == int and type(second_value) == int:
        return first_value * second_value
    else:
        raise ValueError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"

    """
    try:
        return int(first_value) * int(second_value)
    except ValueError:
        raise ValueError


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
   return word in text


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    num = [6, 7]
    l = []
    for n in range(13):
        if n in num:
            continue
        l.append(n)
    return l


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    l = []
    for n in data:
        if n < 0:
            continue
        l.append(n)
    return l


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    alf = [c for c in ascii_lowercase]
    keys = [i for i in range(1, len(ascii_lowercase)+1)]
    d = dict(zip(keys, alf))
    return d


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    for i in range(len(data), 0, -1):
        for j in range(1, i):
            if data[j - 1] > data[j]:
                tmp = data[j - 1]
                data[j - 1] = data[j]
                data[j] = tmp
    return data

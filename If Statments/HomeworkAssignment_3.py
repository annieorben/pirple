"""
Course:     Python Is Easy
Assignment: Homework assignment 3 for the If Statements lecture.
Purpose:    To practice using different forms of the "If" statement.
"""

from collections import Counter


def sort_of_equal(*args):
    """
    Returns a boolean indicating if exactly 2 of the method arguments are the same number.
    For extra credit the map function will turn each argument into a string before being counted.

    """
    return [v for v in Counter(map(str, args)).values() if v == 2] != []


first_test = "sort_of_equal(1, 2, 3)"
print(first_test, eval(first_test))

second_test = "sort_of_equal(1, 1, 2)"
print(second_test, eval(second_test))

third_test = "sort_of_equal(1, 1, 1)"
print(third_test, eval(third_test))

fourth_test = "sort_of_equal('1', 1, 2)"
print(fourth_test, eval(fourth_test))

fifth_test = "sort_of_equal('car', 'apple', 3, 'car')"
print(fifth_test, eval(fifth_test))

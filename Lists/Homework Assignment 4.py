"""
# Course:     Python Is Easy.
# Assignment: Homework assignment 4 for the lists lecture.
# Purpose:    To practice using lists in a few basic scenarios.
"""
from collections import Counter

myUniqueList = []
myLeftovers = []


def add_things_to_my_unique_list(values):
    """
    # The purpose of this method is to fill myUniqueList with unique values from the values collection defined in the
    # parameter. Additionally, any non-unique values are passed into the add_thing_to_my_leftovers method.
    # :param values: tuple
    # :return:
    """
    [myUniqueList.append(value) for value in set(values)]
    [add_thing_to_my_leftovers(value) for value in Counter(values).items() if value[1] > 1]


def add_thing_to_my_leftovers(value):
    """
    # The purpose of this method is to add count * non-unique value to the myLetovers collection.
    # :param value:
    # :return:
    """
    x = 1
    while x < value[1]:
        myLeftovers.append(value[0])
        x += 1


def test_list(*args):
    """
    # The purpose of this method is do a bit of housekeeping when running each test case. The method under test is
    # called directly followed by outputting the resulting program state and then initializing the program for any
    # subsequent test cases.
    # :param args:
    # :return:
    """
    add_things_to_my_unique_list(args)
    print('original =', args, 'myUniqueList =', myUniqueList, 'myLeftovers =', myLeftovers)
    myUniqueList.clear()
    myLeftovers.clear()


test_list(1, 2, 3)
test_list(1, 2, 3, 2, 4)
test_list(1, 2, 3, 2, 4, 4, 4, 4)
test_list("boat", "lemon", "pair", "pair", "14")

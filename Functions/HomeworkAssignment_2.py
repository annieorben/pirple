"""
Course:     Python Is Easy
Assignment: Homework assignment 2 for the Functions lecture.
Purpose:    To practice using functions to return data.
"""


def artist():
    return "Helen Jane Long"  # Returning a string when executing the Artist attribute.


def genre():
    return "Vocal/Easy Listening"  # Returning a string when executing the Artist attribute.


def performers():
    return ["Helen Jane Long (Cello)", "Jonathan Hill (Viola)", "Jonathan Hill (Violin)"]  # Returning Performers list


def find_sub_string(query):
    """Extra credit: using a boolean in a function."""
    result = []  # create an empty list to collect results
    for func in [artist, genre, performers]:  # iterate over functions
        """
        This one's a bit more complicated. We're looking for either the query contained in just a string or if a list 
        is returned then we're looking for any occurrence of the query in s to be True where s is each element of the 
        list returned by func() in the list comprehension.
        """
        if query in func() or any(query in s for s in func()):
            result.append(func())  # When a match is found add it to the result list.
    return len(result) > 0, result  # Returns tuple indicating True if found and what was found, or false if not found


for qry in ['Cello', 'Widget', 'Helen']:  # Iterating over a collection of queries.
    print(find_sub_string(qry))  # Printing the result of each query.

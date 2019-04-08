"""
Course: Python Is Easy
Assignment 1: Homework assignment for the Variables lecture.
Purpose:    To practice using variables, assignments and print statements in a scripting fashion.
            The application assigns different types of values to globally defined variables.
            It
"""
Artist = "Helen Jane Long"
Album = "Porcelain"
PlayTimeSeconds = (3 * 60) + 42  # 3 minutes 42 seconds
Genre = "Vocal/Easy Listening"
Performers = ["Helen Jane Long (Cello)", "Jonathan Hill (Viola)", "Jonathan Hill (Violin)"]
Period = "20th Century"
Venue = "BLE Music Studios, Tennessee (05/2006 - 09/2006)"
Publisher = "Warner Music Group"

print("Artist = " + Artist)
print("Album = " + Album)
""" 
Python does not do implicit type conversions to the arguments provided to the '+' operator. I chose to do an explicit 
conversion to work with the default implementation of __add__() which is what '+' maps to.
"""

print("PlayTimeSeconds = " + str(PlayTimeSeconds))
print("Genre = " + Genre)
"""The list type does not have a __str__() definition which would be called by the print() method. But the list does 
have the __repr__() defined which can be called explicitly to generate a more development oriented string representation
of the list. So I turned the list into a string with repr(Performers) and concatenated string to string in the print 
method."""
print("Performers = " + repr(Performers))
"""Alternatively it is also possible to pass a list into print() as a positional argument without the concatenation. 
This will look first for the __str__() for the list type. Failing to find a definition Python would fail over to the 
__repr__() which is defined."""
print("Performers =", Performers)
print("Period = " + Period)
print("Venue = " + Venue)
print("Publisher = " + Publisher)

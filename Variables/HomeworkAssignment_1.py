"""
Course:     Python Is Easy
Assignment: Homework assignment 1 for the Variables lecture.
Purpose:    To practice using variables, assignments and print statements in a scripting fashion.
            The application assigns different types of values to globally defined variables.
"""
Artist = "Helen Jane Long"  # Assigning a string to the Artist variable
Album = "Porcelain"  # Assigning a string to the Album variable
Title = "Expression"  # Assigning a string to the Title variable
PlayTimeSeconds = (3 * 60) + 42  # Assigning 3 minutes 42 seconds to the PlayTimeSeconds variable as the total seconds
Genre = "Vocal/Easy Listening"  # Assigning a string to the Artist variable
Performers = ["Helen Jane Long (Cello)", "Jonathan Hill (Viola)", "Jonathan Hill (Violin)"]  # Assigning Performers list
Period = "20th Century"  # Assigning a string to the Period variable
Venue = "BLE Music Studios, Tennessee (05/2006 - 09/2006)"  # Assigning a string to the Venue variable
Publisher = "Warner Music Group"  # Assigning a string to the Publisher variable

print("Artist = " + Artist)  # print is a builtin attribute which points to a value of type method
print("Album = " + Album)  # print also defaults to writing to the sys.stdout stream.
print("Title = " + Title)
""" 
Python does not do implicit type conversions to the arguments provided to the '+' operator. I chose to do an explicit 
conversion to work with the default implementation of __add__() which is what '+' maps to.
"""

print("PlayTimeSeconds = ", PlayTimeSeconds, sep=' ')
print("Genre = " + Genre)
"""The list type does not have a __str__() definition which would be called by the print() method. But the list does 
have the __repr__() defined which can be called explicitly to generate a more development oriented string representation
of the list. So I turned the list into a string with repr(Performers) and concatenated string to string in the print 
method."""
print("Performers = " + repr(Performers))
"""Alternatively it is also possible to pass a list into print() as a positional argument without the concatenation. 
This will look first for the __str__() for the list type. Failing to find a definition Python fails over to the 
__repr__() which is defined for the list type."""
print("Performers =", Performers)  # Notice the '+' symbol is replaced by a comma for the positional arguments.
print("Period = " + Period)
print("Venue = " + Venue)
print("Publisher = " + Publisher)

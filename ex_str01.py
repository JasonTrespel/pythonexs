#!/usr/bin/env python3

"""practice with splicing string values"""

# create string
string1 = "This is my first example!"

# Showing that even strings have position values
print(string1[5:16])

# showing strings can be repeated by adding multipliers
print(string1*3)

# create second string
string2 = "This is my second example!"
# see results from split argument
string2 = str.split(string2)
print(string2)

# MAKING EVERYTHING CAPITAL
string2 = str.upper(string1)
print(string2)

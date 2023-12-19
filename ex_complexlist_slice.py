#!/usr/bin/env python3
"""Simple example of slicing complex lists (sub-lists)"""

# start with a list
simplelist = ["yours", "mine", "ours"]

# print simplelist to show data for reference
print(simplelist)

# create a complex list. 
# turn 123 into separate list
complexlist = [1, 2, 3, ["owl", "bear", "lizard"]]

# print complexlist to show data for reference
print(complexlist)

# slice through complexlist example
print(complexlist[3][1])

# what happens if we concatenate them
print(simplelist + complexlist)

# let's make it easier
newlist = simplelist + complexlist
print(newlist, end="\n")

# print one more example
print(newlist[4])
print(newlist[6][0])

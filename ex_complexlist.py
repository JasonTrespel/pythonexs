#!/usr/bin/env python3

"""create a complex list from a simple list"""

# state simple list and print 
simplelist = ["oil", "car", "gas"]
print(simplelist)
print(simplelist[1])

# add new item
simplelist.append("taxi")

# print out list to see new item
print(simplelist)

# add new list item to list
simplelist.append(["cone", "stoplight", "battery"])

# print out extended list
print(simplelist)

# start slicing
print(simplelist[4][2])

# add EVEN MORE
simplelist.append(["green", "blue", 17])
print(simplelist)

# MORE SPLICE
print(simplelist[4][0], simplelist[5])
print(simplelist[4][0], simplelist[5][2])

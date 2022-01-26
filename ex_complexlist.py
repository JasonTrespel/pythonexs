#!/usr/bin/env python3

# create a complex list from a simple list
# simple list
simplelist = ["oil", "car", "gas"]
print(simplelist)
print(simplelist[1])

# add new item
simplelist.append("taxi")
# print out list 
print(simplelist)

# add new list to list
simplelist.append(["cone", "stoplight", "battery"])
# print out list
print(simplelist)

# start slicing
print(simplelist[4][2])

# add EVEN MORE
simplelist.append(["green", "blue", 17])
print(simplelist)

# MORE SPLICE
print(simplelist[4][0], simplelist[5])
print(simplelist[4][0], simplelist[5][2])

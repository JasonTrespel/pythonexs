#!/usr/bin/env python3
  
import netifaces

print(netifaces.interfaces())

# user needs to choose which adapter to get the MAC addr from
inter = input("Which interface would you like to see the MAC address? ")

print(netifaces.ifaddresses(inter))

print("\n")
# let's borrow a line from lab 23
print("MAC: ", end="")
print((netifaces.ifaddresses(inter)[netifaces.AF_LINK])[0]["addr"])

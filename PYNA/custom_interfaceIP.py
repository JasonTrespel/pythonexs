#!/usr/bin/env python3
  
import netifaces

print(netifaces.interfaces())

# user needs to choose which adapter to get the IP from
inter = input("Which interface would you like to see the IP address? ")

print(netifaces.ifaddresses(inter))

print("\n")
# let's borrow a line from lab 23
print("IP: ", end="")
print((netifaces.ifaddresses(inter)[netifaces.AF_INET])[0]["addr"])

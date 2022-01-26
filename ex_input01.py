#!/usr/bin/env python3

# setting variable
color = "white"

# will ask for favorite color 
question = input("What is your favorite color?")

# will print statement giving answer
print(f"You said your favorite color is {question}!")

# python gives a response
print("That's a cool color! My favorite is white.")

# gives a response but using concatenation.
print("That's a cool color! My favorite is " + color)

# update variable
color = "purple"
# print new response
print("Never mind! It is actually" + color)

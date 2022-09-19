#!/usr/bin/python3

"""Ask for a user name, ask what day of the week it is, print: Hello, <name>! Happy <day of the week>!"""


# let's follow best practice here
# define the main function
def main():

    # ask for the user's name
    name = input("What is your name?")

    # aks for the day of the week
    day = input("What is today?")

    # print returning statement
    print("Hello," + name)
    # there was a spacing issue, let's fix that
    print("Hello, " + name + "!")

    # print out day of the week
    print("Happy " + day + "!")

    # now I want to use an f string instead of concatenate
    print(f"Hello, {name}! Happy {day}!")


# call the main function
if __name__ == "__main__":
    main()

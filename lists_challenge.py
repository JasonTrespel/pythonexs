#!/usr/bin/env python3

"""following directions of lists challenge"""

def main():

    # start off with our variables
    wordbank = ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon",
                  "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]


    # append 4 to list wordbank
    wordbank.append(4)
    print(wordbank)

    # input asking for number from 0-18
    num = input("Hey you! Choose a number between 1 and 18! Please and thanks. ")

    # convert num variable into an integer
    int(num)

    # useing num, splice through one element from tlgstudents
    user_made = int(input("Actually I could use another number between 0 and 18! "))
    student_name = tlgstudents[user_made]

    # print last statement
    print(f"{student_name} always uses {num} spaces to indent.")
    


if __name__ == "__main__":
    main()

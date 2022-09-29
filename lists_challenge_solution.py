#!/usr/bin/env python3
""" Alta3 Research | TPatrick
    Lists Challenge """

import random

def main():

    wordbank = ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif",
                  "Brent", "Cedric", "Chris",
                  "Cory", "Ebrima", "Franco",
                  "Greg", "Hoon", "Joey",
                  "Jordan", "JC", "LB",
                  "Mabel", "Shon", "Pat", "Zach"]

    print(tlgstudents)
    wordbank.append(4)
    print(wordbank)

    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]

    print(f"Your unfortunate victim is {name}!")
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    name = random.choice(tlgstudents)
    print(f"{name}")

main()

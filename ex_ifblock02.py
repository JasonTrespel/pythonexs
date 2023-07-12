#!/usr/bin/env python3

"""Giving letter grades based on number score."""
# code is not perfect. Things that can be improved: script can continue if person enters "y" or "n"

# set up a statement for explanation
results = "your letter grade is "

def main():
    # ask user for input
    name = input("What is your name? ")

    cont = input("Would you like to enter a number score and see your grade? 'yes' or 'no' ")

    # Set up a while loop to keep asking for user scores.
    """The while loop will continure to ask user if they want to continue entering scores."""
    while cont == "yes":

        # notice the input has been wrapped within a float function
        score = float(input("What is your score? "))
    
        # if input is higher than or equal to 90
        if score >= 90:
            final_results = name + ", " + results + "A! Amazing job!"
            print(final_results)
            cont = input("Would you like to enter a number score and see your grade? 'yes' or 'no' ")
            if cont == "no":
                print("Oh, alright. Maybe next time.")
                break

        # if input is higher than or equal to 80
        elif score >= 80:
            final_results = name + ", " + results + "B! Great job."
            print(final_results)
            cont = input("Would you like to enter a number score and see your grade? 'yes' or 'no' ")
            if cont == "no":
                print("Oh, alright. Maybe next time.")
                break

        # if input is higher than or equal to 70
        elif score >= 70:
            final_results = name + ", " + results + "C. Cs get Degrees."
            print(final_results)
            cont = input("Would you like to enter a number score and see your grade? 'yes' or 'no' ")
            if cont == "no":
                print("Oh, alright. Maybe next time.")
                break

        # if input is higher than or equal to 60
        elif score >= 60:
            final_results = name + ", " + results + "D. Room for improvment."
            print(final_results)
            cont = input("Would you like to enter a number score and see your grade? 'yes' or 'no' ")
            if cont == "no":
                print("Oh, alright. Maybe next time.")
                break

        # all other lower integers
        else:
            final_results = name + ", " + results + "E. For extra failure."
            print(final_results)
            cont = input("Would you like to enter a number score and see your grade? 'yes' or 'no' ")
            if cont == "no":
                print("Oh, alright. Maybe next time.")
                break

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""A script to show off 'sep' and 'end' parameters."""\

def main():
    """Use multiple print functions to show 'sep' and 'end' params"""

    # start with basic example. first without param
    print("Columbus, Ohio")
    # then with a param
    print("Columbus", "Ohio", sep=", ")

    # print empty space 
    print("")
    
    # basic example of end param
    print("Columbus", end=", ")
    print("Ohio")

    # next example is for longer print examples
    # create variable for print
    example_string = "I live in Columbus Ohio."

    # example of using sep param
    print("\n")
    print(example_string)
    print("Welcome", "to", "Columbus.", sep="\t")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""Create a list of at least five animals with three letter names and have your program output them to the screen."""

# create the main function
def main():

    # start with creating a list; 5 animals, 3 letter names
    animal_crossing = ["Cat", "Dog", "Sue", "Zig", "Zag", "Fly", "Fox", "Zoe"]

    # print names to screen
    print(animal_crossing)
    # return animal_crossing

    for name in animal_crossing:
        print(name)
    

    # let's print new names
    new_list = [new for new in animal_crossing if new.upper().startswith("Z")]
    print(new_list)

if __name__ == "__main__":
    main()

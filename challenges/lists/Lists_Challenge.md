# EXERCISE: LISTS, INPUT, PRINT, VARIABLES

<img src="https://i.redd.it/wk843smkri441.jpg" alt="drawing" width="400"/>

**Objective:** Add the following components to your code in this order:

**PART 1.** Put this list in your code:   

```python
wordbank= ["indentation", "spaces"] 
```

**PART 2.** Put this list in your code:   

```python
tlgstudents= ["Aaron", "Ahmed", "Andy", "Brent", "Cedric", "Chris", "Dom", "Franco", "John", "Nicolas", "Joey", "Jordan", "JC", "Louis", "Samuel", "Sanam", "Zach"]
```
    
**PART 3.** Add a line of code that appends the integer `4` to the list `wordbank`.

<details>
<summary>I need a hint!</summary>
<br>
    
    wordbank.append(4)
</details>

**PART 4.** Include an input asking for a number between 0 and 17. Save this as the variable `num`.

<details>
<summary>I need a hint!</summary>
<br>
    
    num= input("Pick a student number!")
</details>

**PART 5.** Remember that *input()* always returns a string... convert `num` into an integer!

<details>
<summary>I need another hint!</summary>
<br>
    
    num= int(input("Pick a student number!"))
</details>

**PART 5.** Use the integer `num` to slice one of the elements from the list `tlgstudents`. Save the name you return as the variable `student_name`.

<details>
<summary>MOAR HINTZ!</summary>
<br>
    
    choice= int(input("Pick a student number!"))
    student_name= tlgstudents[choice]
</details>

**PART 6.** Using elements from the `tlgstudents` list and the `student_name` string, print this output.

```
<student_name> always uses <4> <spaces> to indent.
```
> "4" and "spaces" should come from `wordbank`!

**Bonus 1** 

Find a way to randomize what student name is picked. 
HINT: There is a function for this; don't be afraid to look for answers on the docs page!


**Bonus 2**

The list of students for the course is consistently changing. Class sizes can expand or diminish with each teaching (although the expectation is that classes will grow!). Set the `num` variable to account for changing list lengths, without having to manually recode the list range. Finally, code the input() to allow the user to type a number beginning from 1 (users don't like to think about zero-indexing). Hint - Check the Python built-in functions.



## SOLUTION Including Bonuses:

<details>
<summary>Solution is below if you find yourself stuck.</summary>
<br>
  
```python
#!/usr/bin/env python3
""" Alta3 Research | TPatrick
    Lists Challenge """

# import random module
import random

def main():
    
    # enter variable data
    wordbank = ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif",
                  "Brent", "Cedric", "Chris",
                  "Dom", "Franco", "Ripal",
                  "Rod", "Joey", "Jordan",
                  "JC", "Louuis", "Samuel",
                  "Thomas", "Zach"]

    # print the tlg list as shown above. This helps to compare differences later implemented.
    print(tlgstudents)
    
    # append the integer 4 to the wordbank list and then print the new list
    wordbank.append(4)
    print(wordbank)
    
    # for Bonus 2. Student name printed out below is related to input from user.
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]
    
    
    print(f"Your unfortunate victim is {name}!")
    # print here is pulling variable data from wordbank list as well as 'name' set above
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    
    # for Bonus 1, from the random library, .choice is used to pick a random student name and printed out
    name = random.choice(tlgstudents)
    print(f"{name}")

if __name__ == "__main__":
    main()
```
</details>

#!/usr/bin/env python3

### Giving letter grades based on number score.

# set up a statement for explanation
results = 'Your letter grade is '

# notice the input has been wrapped within a float function
score = float(input("What is your score?"))

# if input is higher than or equal to 90
if score >= 90:
    final_results = results + 'A! Amazing job!'
    
# if input is higher than or equal to 80
elif score >= 80:
    final_results = results + 'B! Great job.'
    
# if input is higher than or equal to 70
elif score >= 70:
    final_results = results + 'C. Cs get Degrees.'
    
# if input is higher than or equal to 60
elif score >= 60:
    final_results = results + 'D. Room for improvment.'
    
# all other lower integers
else:
    final_results = results + 'E. For extra failure.'

print(final_results)

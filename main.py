# Hello Print Function
"""[Code Here]
print('Hello ' + input('What is Your Name ' + " " + 'Nice to meet you \n')
"""
# Hello Input Function
'''[Code Here]
print('What is your favorite food')
food = input()
print('Your favorite food is ' + food + '\n')
print(len(food))
'''
# Hello string data type with array
'''[Code Here]
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
'''
# Hello input string data type Then I converted 2 number into int and printed the sum
# Assuming the input is always a two-digit number
'''[Code Here]
two_digit_number = input()
print(type(two_digit_number))
print(two_digit_number[0] + two_digit_number[1])
print(int(two_digit_number[0]) + int(two_digit_number[1]))
print(type(two_digit_number))
'''

# Calculations Mode


# PEMDAS
# Parenthesis ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -
# floor division //
'''[note]
PEMDAS is an acronym that stands for the order of operations in mathematics. It helps to determine the sequence in which various mathematical operations should be performed to evaluate an expression. PEMDAS stands for:

1. P: Parentheses - Perform operations inside parentheses first.
2. E: Exponents - Evaluate exponentiation (i.e., powers and roots).
3. MD: Multiplication and Division - Perform multiplication and division from left to right.
4. AS: Addition and Subtraction - Perform addition and subtraction from left to right.

Following the PEMDAS order ensures that mathematical expressions are evaluated correctly and consistently. Here's an example of how PEMDAS is applied:

1. Solve 3 + 2 x (4 - 1)^2.

   Applying PEMDAS:
   1. Start with parentheses: 4 - 1 = 3.
   2. Next, exponentiation: 3^2 = 9.
   3. Then, multiplication: 2 x 9 = 18.
   4. Finally, addition: 3 + 18 = 21.

So, the expression evaluates to 21, following the PEMDAS order.
'''

# Comparison Operators
# Modulus %
# Floor Division //
# Assignment =
# Less than <
# Greater than >
# Less than or equal to <=
# Greater than or equal to >=
# Equal to ==
# Not Equal to !=
# And Operator and (&&)
# Or Operator or (||)
# Not Operator not (!)
# Logical Operators
'''
print('Welcome to Calculator App')
print(3*3+3/3-3)
print(int(3*3+3/3-3))
'''
# BMI = weight (kg) / height (m) x height (m)
# e.g. weight = 72 kg, height = 1.65 m
# BMI = 72 kg / (1.65 x 1.65) = 26
#  Don't change the code above
'''[Code Here]
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_c = float(height)
weight_c = int(weight)
bmi = weight_c / (height_c**2)
print(int(bmi))
if (bmi < 18.5):
  print("Underweight")
elif (bmi >= 18.5 and bmi <= 24.9):
  print("Normal")
elif (bmi >= 25 and bmi <= 29.9):
  print("Overweight")
else:
  print("Obese")
'''
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# one year has 52 weeks
# one week has 7 days
# one day has 24 hours
# one hour has 60 minutes
# one minute has 60 seconds
# one second has 1000 milliseconds
#  Don't change the code above 
# Write your code below this line 
'''
age = input()
age_in_w = int(age) * 52
age_in_d = age_in_w * 7
age_in_h = age_in_d * 24
age_in_m = age_in_h * 60
age_in_s = age_in_m * 60
age_in_ms = age_in_s * 1000
print(age_in_w)
print(age_in_d)
print(age_in_h)
print(age_in_m)
print(age_in_s)
print(age_in_ms)
'''
'''
life_Remain_weeks = (90-int(age))*52
print(f"You have {life_Remain_weeks} weeks left.")
'''

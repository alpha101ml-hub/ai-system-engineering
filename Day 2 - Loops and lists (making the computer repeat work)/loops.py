# This is a comment - Python ignores it
# It's just a for humans to read

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)
    
'''
for i in range(1, 6): means: "Create a variable i that takes the values 1, 2, 3, 4, 5 (the number 6 is not included – it's the stopping point)."

For each value, run the print(i) line.

This is a loop – it repeats.
'''

# For range(10, 21): "Create a variable i that takes the values 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 (the number 21 is not included)."
print("For range in range(10, 21)")
for i in range(10, 21):
    print(i)
    
# Lists - storing multiple things

# A list of fruits
fruits = ["apple", "banana", "cherry"]
print("My fruits:")
for fruit in fruits:
    print(fruit)
    
'''
What is a list?
A list is a container that holds multiple values. ["apple", "banana", "cherry"] is a list of three strings. The for loop goes through each one.
'''

# Conditionals - making decisions (if/else)

# Check if a number is even or odd
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
    
'''
What is %?
It's the modulo operator – it gives the remainder after division.
7 % 2 is 1 (because 7 divided by 2 leaves remainder 1).
If remainder is 0, the number is even.
'''

number = 10
if number % 2 ==0:
    print(number, "is even")
else:
    print(number, "is odd")
    
# First real exercise - FizzBuzz
for i in range(1, 21):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
        
# FizzBuzz if you can combine loops, conditionals and modulo arithmetic. Many beginners can't do it. You just did.
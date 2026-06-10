'''
Modules are like toolboxes - they contain pre-written code. The random module gives you functions for random numbers.
'''


# Import the random module
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

'''
What does random.randint(1, 100) do ?
It returns a random integer between 1 and 100 (inclusive). Each time you run the program, you'll get a different number.

Test it: secret_number temporily to see it works. Delete that line later.
'''

# print(secret_number)

'''
A while loop repeats as long as a condition is true. We'll keep guessing until the user is correct.
'''

# Initialize variable 
guesses_taken = 0
correct = False

while not correct:
    try:
        # Get the user's guess
        guess = input("Take a guess: ")
        guess = int(guess)  # convert to integer
        guesses_taken = guesses_taken + 1

        # Check the guess 
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Good job! You guessed it in {guesses_taken} tries.")
            correct = True  # this wil exit the loop
    except ValueError:
        print("Please enter a valid number.")
        
        
'''
Explanation:
- while not correct: means "keep looping while correct is False"
- guesses_taken counts each guess
- When the guess matches, we set correct = True, which stops the loop.
- f"..." is an f-string -- it inserts variables into the string.
'''

# If the user types letters instead of numbers, the program crashes, add try/except.
import random

print("Welcome to the Number Guessing Game!")
print("I'll think of a number between 1 and 100.")

play_again = "yes"

while play_again == "yes":
    secret_number = random.randint(1, 100)
    guesses_taken = 0
    correct = False
    
    print("\nI have my number. Start guessing!")
    
    while not correct:
        try:
            guess = input("Your guess: ")
            guess = int(guess)
            guesses_taken += 1
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! You got it in {guesses_taken} guesses.")
                correct = True
        except ValueError:
            print("Numbers only, please.")
        
    # Ask to play again
    play_again = input("\nPlay again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Please say 'yes' or 'no': ").lower()
                    
print("Thanks forn playing!")
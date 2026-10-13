# Number Guessing Game
# AI Enginerring - AM

import random # Imports the random module so that we can generate random numbers

random_number = random.randint(1,10) # Generates a number between 1 and 10

previous_guesses = [] # Creating an empty list to store user's previous guesses

correct_answered_picked = False # Guess is incorrect

while correct_answered_picked == False: # Continues until the user guesses correctly
    user_guess = int(input("Enter a number between 1-10: ")) # Asking the user to guess

    while user_guess < 1 or user_guess > 10 or user_guess in previous_guesses: # Making sure that the user chooses a number between 1 and 10 and number has already guessed
        if user_guess < 1 or user_guess > 10: # Checks if outside range
            print("Invalid input!") # Tells user that their guess in invalid
        else: 
            print("You have already guessed", user_guess + "! Choose a different number") # They have already guessed that number
            print("Previous guesses:", previous_guesses) # Shows the guesses stored
            user_guess = int(input("Enter a number between 1-10: ")) # Asking the user to guess
    
    previous_guesses.append(user_guess) # Adding a new guess to the list

    if user_guess == random_number: # If the guess match the number
        print("You guessed correctly!")
        correct_answered_picked = True # The correct guess

    elif user_guess > random_number: 
        print("Try again! The random number is lower!") # Telling the player to guess lower
        print("Previous guesses:", previous_guesses)

    else:
        print("Try again! The random number is higher!") # Telling the player to guess higher
        print("Previous guesses:", previous_guesses) # Shows the guesses stored

print("Your guesses:", previous_guesses)
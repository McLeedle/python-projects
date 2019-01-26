# guess the number game
import random

print "Welcome to guess the number!"
print "You have 10 tries to guess the correct number!"
print "The range of numbers will be from 0-25"

# variables to store winning number, user guess and number of tries
number = random.randint(0, 25)
guess = raw_input("Please enter a number (0-25): ")
tries = 0

# check to see if the user guessed the right number
if int(guess) == number:
    print "Congratulations you\'ve won!"

# noticed that you could input invalid numbers and it counted as a guess so this is how i solved that
while int(guess) > 25 or int(guess) < 0:
    guess = raw_input("Please enter a VALID guess: ")
else:
    # my attempt at making the game loop
    while tries < 10 and int(guess) != number:
        guess = raw_input("Please guess again: ")
        tries = tries + 1
        # i noticed if i guessed the right answer out of the loop it would just exit so i duplicated here to prevent it
        if int(guess) == number:
            print "Congratulations you\'ve won!"
        # implemented the lose mechanic
        elif tries == 10:
            print "You've Lost!"
        # same with the correct answer issue i had so i put it in the loop as well
        elif int(guess) > 25 or int(guess) < 0:
            while int(guess) > 25 or int(guess) < 0:
                guess = raw_input("Please enter a VALID guess: ")
                # this is here because I didn't want to take tries away for invalid guesses
                tries = tries

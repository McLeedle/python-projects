# guess the number game
from random import randint

print "Welcome to guess the number!"
print "You have 10 tries to guess the correct number!"
print "The range of numbers will be from 0-25"

# variables for the game
LO, HI = 0, 25
MAX_TRIES = 10


def main():
    # generate random number each game
    answer = randint(LO, HI)

    for _ in range(MAX_TRIES):
        guess = get_guess()

        if guess == answer:
            print "You Win!"
            break
    if MAX_TRIES == 10:
        print "Too many tries. You Lose!"


def get_guess():
    while True:
        try:
            guess = int(raw_input("Please enter a number (0-25): "))
        except ValueError:
            print "Please enter a number: "
        else:
            if LO <= guess <= HI:
                return guess
            print "Please enter a number between %s and %s" % (LO, HI)


main()

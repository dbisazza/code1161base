"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
import random


def advancedGuessingGame():
    """Play a guessing game with a user.
    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nwelcome to the guessing game!")
    lowerBound = raw_input("Enter an lower bound: ")
    upperBound = raw_input("Enter an upper bound: ")
    print("OK then, a number between %s and %s ?" % (lowerBound, upperBound))
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)

    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False

    def asknumber(lo, hi):
        Test = False
        my_num = "Test"
        Quest = "Enter a number between "

        while Test is False:
            try:
                my_num = 2
                Test2 = int(my_num)
                Test = True
                my_num = int(raw_input("%s%s and %s:" % (Quest, lo, hi)))
                while not lo <= my_num <= hi:
                    my_num = int(raw_input("%s%s and %s:" % (Quest, lo, hi)))
            except ValueError:
                print("That's not a valid entry!")
                Test = False
            return(Test2)
            print("you guessed {},".format(Test2),)

    while not guessed:
        guessedNumber = asknumber(lowerBound, upperBound)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()

import random

print("Welcome to Number Guessing Game")
print("I am thinking of a number between 0 to 100")
difficulty_level = input("Choose a difficulty level... 'easy' or 'hard' ").lower()
NUMBER_OF_TURNS = 0

if difficulty_level == "easy":
    NUMBER_OF_TURNS = 10
else:
    NUMBER_OF_TURNS = 5


def guessNumber():
    generated_Number = random.randint(1, 100)
    global NUMBER_OF_TURNS
    while NUMBER_OF_TURNS > 0:
        guessNumber = int(input("Guess Number"))
        if not (guessNumber == generated_Number) and guessNumber > generated_Number:
            print("High")

            NUMBER_OF_TURNS -= 1
        elif not (guessNumber == generated_Number) and guessNumber < generated_Number:
            print("Low")

            NUMBER_OF_TURNS -= 1
        else:
            print("You Won")
            break

        if NUMBER_OF_TURNS==0:
            print("You loose")

guessNumber()
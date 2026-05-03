# Guess the Number Game

import random


# generate random number
secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to Guess the Number Game!")
print("Guess a number between 1 and 100")


while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Correct! You guessed in", attempts, "attempts")
        break

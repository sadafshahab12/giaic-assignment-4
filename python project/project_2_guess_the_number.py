# Guess the Number Game
import random


def guess(a):
    random_number = random.randint(1, a)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {a}: "))
        if guess < random_number:
            print("Sorry, guess again. Too Low")
        elif guess > random_number:
            print("Sorry, guess again. Too High")

    print(f"Yay, congrats, you have guess the number {random_number} correctly.")


guess(10)

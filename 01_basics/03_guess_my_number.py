# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

import random

guess_number = random.randint(0, 99)


def main():
    user_guess = int(input("Enter a guess: "))
    while user_guess != guess_number:
        if user_guess > guess_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        print()
        user_guess = int(input("Enter a new number: "))
    print(f"Congrats! The number was: {guess_number}")


if __name__ == "__main__":
    main()

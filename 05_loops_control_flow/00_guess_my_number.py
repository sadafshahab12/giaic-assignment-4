# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

import random
def main():
    computer_generated_guess = random.randint(1, 99)
    print("I am thinking of number between 1 and 99")
    user_guess = int(input("Enter a guess: "))
    while user_guess != computer_generated_guess:
        if user_guess < computer_generated_guess:
            print("you guess is too low")
        else:
            print("you guess is too high")

        print()
        user_guess = int(input("Enter a guess: "))
    print(f"Congrats! The number was {computer_generated_guess}")


if __name__ == "__main__":
    main()

# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.
import random

ROUND = 5
def main():
    print("Welcome to high low game!")
    print("-----------------------------------------------")
    your_score = 0
    for i in range(ROUND):
        print(f"Round: {i + 1}")
        print("-----------------------------------------------")
        computer_num = random.randint(1, 100)
        your_number = random.randint(1, 100)
        print(f"Your number is {your_number}")
        user_choice = input(
            "Do you think your number is higher or lower than the computer's? "
        )
        while user_choice != "higher" and user_choice != "lower":
            user_choice = input("Please Enter either higher or lower! ")
        higher_and_correct = user_choice == "higher" and your_number > computer_num
        lower_and_correct = user_choice == "lower" and your_number < computer_num
        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
        else:
            print(f"Aww that's incorrect. The computer's number was {computer_num}")
        print(f"Your current store is {your_score}")
        print()

    print(f"You final score is {your_score}")
    if your_score == ROUND:
        print("Wow! You played perfectly!")
    elif your_score > ROUND // 2:
        print("Good job , You played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()

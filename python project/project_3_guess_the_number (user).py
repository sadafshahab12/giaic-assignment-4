# Guess the Number Game
import random


def comp_guess(a):
    low = 1
    high = a
    feedback = ""
    while feedback != "c":
        if low != high:   
            guess = random.randint(low ,high)
        else:
            guess = low
        feedback = input(f"Is {guess} to high (H) , too low (L) or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay, The computer guess your number {guess} correctly.")
  


comp_guess(10)

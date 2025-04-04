# variable scope 
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

num_sides = 6  # Number of sides on the dice  #variable scope


def roll_dice():
    """Simulate rolling two dice and return the results."""
    die_1 = random.randint(1, num_sides)
    die_2 = random.randint(1, num_sides)
    print(f"Die 1: {die_1} , Die 2: {die_2}")
    total = die_1 + die_2
    print(f"Total : {total}")


def main():
    # die_1 = 10 
    """Roll dice three times"""
    roll_dice()
    roll_dice()
    roll_dice()
    # print(die_1)


if __name__ == "__main__":
    main()

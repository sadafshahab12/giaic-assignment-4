# Simulate rolling two dice, and prints results of each roll as well as the total.

import random
num_side = 6
def main():
    die_1 = random.randint(1, num_side) #generate a random number b/w 1 to 6 in die_1
    die_2 = random.randint(1, num_side) #generate a random number b/w 1 to 6 in die_2
    sum_of_two_dice = die_1 + die_2
    print(f"Die 1 : {die_1}")
    print(f"Die 2 : {die_2}")
    print(f"Total : {sum_of_two_dice}")


if __name__ == "__main__":
    main()

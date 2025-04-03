import random

random_number = random.randint(1, 10)
print(random_number)

toys = ["car", "doll", "ball", "bunny", "teddy bear", "chick"]
print(random.choice(toys))
print(random.randint(0, len(toys) - 1))
print(random.choice(range(len(toys))))

# name = "sadaf"
# print(random.choice(name))
# Question 1
# Write a program that generates a random number between 1 and 10 (inclusive) and prints it.

random_numbers = random.randint(1, 10)
print(random_numbers)

# Question 2
# Create a list of colors (["red", "green", "blue", "yellow", "purple"]) and write a program that randomly selects a color from the list and prints it.

colors = ["red", "green", "blue", "yellow", "purple"]
print(random.choice(colors))

# Question 3
# Generate a random password of length 8, consisting of uppercase letters, lowercase letters, and digits. Print the password.
import string

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

random_password = random.choices(upper_case + lower_case + digits, k=8)
## string module method
random_password2 = random.choices(
    string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8
)
print(random_password)
print(random_password2)
print("".join(random_password))
print("".join(random_password2))

# Question 4
# Simulate a coin toss by generating a random number (0 or 1). If the number is 0, print "Heads". Otherwise, print "Tails".


def coin_toss():
    coin_toss = random.randint(0, 1)
    print(coin_toss)
    if coin_toss == 0:
        print("Heads")
    else:
        print("Tails")


if __name__ == "__main__":
    coin_toss()


# Question 5
# Create a list of numbers ([1, 2, 3, 4, 5, 6]) and write a program that randomly shuffles the list and prints the shuffled list.

number_Array = [1,2,3,4,5,6]
random.shuffle(number_Array)
print(number_Array)
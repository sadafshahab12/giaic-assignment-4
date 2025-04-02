# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

num1 = input("Enter the first number: ")
num1 = int(num1)
# print(num1)
# print(type(num1))
num2 = input("Enter the second number: ")
num2 = int(num2)
# print(num2)
# print(type(num2))
def add_two_number(num1, num2):
    return num1 + num2


print(add_two_number(num1, num2))

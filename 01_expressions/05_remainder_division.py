# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):
# Please enter an integer to be divided: 5
# Please enter an integer to divide by: 3
# The result of this division is 1 with a remainder of 2

def main():
  first_number = int (input("Enter an integer to be divided: "))
  second_number = int(input("Enter an integer to divide by: "))
  result = first_number / second_number
  remainder = first_number % second_number
  print(f"The result of this division is {result:.2f} with a remainder of {remainder}")
  
if __name__ == "__main__":
  main()
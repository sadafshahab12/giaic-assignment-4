# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
# Here's a sample run of the program (user input in bold italics):
# Enter a number: 2 Double that is 4


def double(num):
    num = num * 2
    return num

def main():
    num = int(input("Enter an integer: "))
    doubled_num = double(num)
    print(f"Double of {num} is: {doubled_num}")


if __name__ == "__main__":
    main()

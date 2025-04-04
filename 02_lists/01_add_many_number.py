# Write a function that takes a list of numbers and returns the sum of those numbers.


def add_many_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def main():
    """take a list of number and return the sum of thos numbers."""
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_of_many_number = add_many_numbers(number)
    print(f"The sum of many number is {sum_of_many_number}")
    
if __name__ == "__main__":
    main()

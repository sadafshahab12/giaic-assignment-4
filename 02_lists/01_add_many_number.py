# Write a function that takes a list of numbers and returns the sum of those numbers.


def add_many_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total  # return the sum of the numbers if we do not return it will be None


def main():
    """take a list of number and return the sum of thos numbers."""
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_of_many_number = add_many_numbers(number)
    print(f"The sum of many number is {sum_of_many_number}")


if __name__ == "__main__":
    main()


def add_numbers(number):
    sum = 0
    for num in number:
        sum += num
    return sum


def result():
    number_array = [1, 2, 3, 4, 5, 6, 78, 9, 10, 11, 12]
    total = add_numbers(number_array)
    print(f"The sum of many number is {total}")


result()

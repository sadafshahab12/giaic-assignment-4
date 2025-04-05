# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]


def main():
    """take a list of number and return the sum of those numbers."""
    number_list = [1, 2, 3, 4]
    doubled_list = []
    for num in range(len(number_list)):
        doubled = number_list[num] * 2
        doubled_list.append(doubled)
    print(f"The doubled list is {doubled_list}")


if __name__ == "__main__":
    main()

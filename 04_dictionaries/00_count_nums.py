# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def get_user_number():
    """Create an empty list to store user input , once they enter a blank line, break the loop and print the list"""
    user_number_list = []
    while True:
        user_input = input("Enter a number: ")
        # if the user do not enter any value break the loop
        if user_input == "":
            break
        user_number_list.append(user_input)
    return user_number_list


def count_nums(num_list):
    """Count the number of times each number appears in a list
    * Create a dictionary to store the count of each number
    * Loop throught the list and count the number of times each number appears
    if the number is not in the dictionary add it as key with a value 1
    if the numbe is in the dictionary increment its value by 1
    """
    num_dic = {}
    for num in num_list:
        if num not in num_dic:
            num_dic[num] = 1
        else:
            num_dic[num] += 1
    print(num_dic)
    return num_dic


def print_count(num_dic):
    """loop over the dic and print out each key and its value"""
    for num in num_dic:
        print(f"{str(num)} appears {str(num_dic[num])} times.")


def main():
    """Ask the user for input and store it in a list, once they enter a blank line, break loop and print the count of number appears."""
    user_num_list = get_user_number()
    num_dict = count_nums(user_num_list)
    print_count(num_dict)


if __name__ == "__main__":
    main()

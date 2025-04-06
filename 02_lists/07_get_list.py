# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def get_list():
    """Prompt the user to enter values one by one and store them in a list"""
    user_list = []
    while True:
        value = input("enter a value: ")
        if value == "":
            break
        user_list.append(value)
    return user_list


def main():
    """Main function to get the list and print it"""
    user_list = get_list()
    print("Here's the list: ", user_list)


if __name__ == "__main__":
    main()


def second():
    user_list = []
    user_input = input("enter a value in number")
    while user_input:
        user_list.append(user_input)
        user_input = input("enter a value in number")
        print(user_list)


if __name__ == "__main__":
    second()

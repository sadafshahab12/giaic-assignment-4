# In this program we show an example of using dictionaries to keep track of information in a phonebook.


def read_phone_numbers():
    phonebook = {}
    while True:
        """use while loop so that user can add many names and contact. if they type done the loop will exit and return a dictionary of phonebook"""
        name = input("Enter a name or done to stop: ")
        if name == "done":
            break
        phone_number = input("Enter the phone number: ")
        phonebook[name] = phone_number
    return phonebook


def print_phonebook(phonebook):
    for name in phonebook:
        print(f"{name} : {phonebook[name]}")


def lookup_for_numbers(phonebook):
    """allow the user to lookup number in the phonebook by looking up the number associated with a name"""
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_for_numbers(phonebook)


if __name__ == "__main__":
    main()

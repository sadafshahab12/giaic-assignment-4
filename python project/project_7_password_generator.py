import random


def main():
    print("Welcome to Password Generator")
    chars = (
        "abcedfghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"
    )
    password_amount = int(input("How many password to generate: "))
    password_length = int(input("Write the length of password to generate: "))

    print("\nHere is your password: \n")

    for pswd in range(password_amount):  # list of passwords
        passwords = ""  # store password in this
        for c in range(password_length):  # password length
            passwords += random.choice(chars)
        print(passwords)


if __name__ == "__main__":
    main()

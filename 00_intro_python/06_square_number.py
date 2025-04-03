# Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0

def main():
  number = float(input("Type a number to see its square: "))
  print(f"\033[3m\033[1m{number}\033[0m is {number **2}\033[0m")

if __name__ == "__main__":
  main()
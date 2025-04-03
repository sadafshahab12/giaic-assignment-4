# Why we use main() 
Think of it like a switch: when you run the program directly, the switch turns on and the code in main() runs. When the program is imported as a module in another program, the switch stays off and the code inside main() does not run.

The if __name__ == "__main__": part helps control when to run your code. If the script is run directly, it will run the code in main(). If it's imported into another script, the code inside main() won't run automatically.

<!-- agreement bot -->
#### Method 1: ANSI Escape Codes

<!-- user_input = input("What is your favourite animal?")

print(f"\n\nMy favourite animal is also \033[1m\033[3m{user_input}!\033[0m") -->

<!-- - \033[1m makes the text bold
- \033[3m makes the text italic
- \033[0m resets the text style -->
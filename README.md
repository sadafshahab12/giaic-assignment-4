# Why we use main()

Think of it like a switch: when you run the program directly, the switch turns on and the code in main() runs. When the program is imported as a module in another program, the switch stays off and the code inside main() does not run.

The if **name** == "**main**": part helps control when to run your code. If the script is run directly, it will run the code in main(). If it's imported into another script, the code inside main() won't run automatically.

agreement bot

#### Method 1: ANSI Escape Codes

user_input = input("What is your favourite animal?")

print(f"\n\nMy favourite animal is also \033[1m\033[3m{user_input}!\033[0m")

\033[1m makes the text bold

- \033[3m makes the text italic
- \033[0m resets the text style

## random

In Python, the random module is like this magic box. It helps you get random results whenever you need them.

## -- Print a random index

random_index = random.randint(0, len(toys) - 1)
print(random_index)

## -- Alternatively, you can use random.choice to select a random index directly

print(random.choice(range(len(toys))))

### Note that random.choice can't be used directly with an integer (like random.choice(0)), because random.choice expects a sequence (like a list or a string) as its argument.

Jab hum random.randint(0, len(toys) - 1) ka istemaal karte hain,
toh yeh humein ek random index deta hai jo 0 se lekar toys ki length minus 1 tak ho sakta hai.

Yeh zaroori hai kyun ki Python mein lists ka indexing 0 se shuru hota hai. Isliye, agar hum len(toys) ka istemaal karte hain, toh humein IndexError mil sakta hai.

Jaise ki, agar toys ki length 5 hai, toh sahi indices hain:

- 0 (pehla element)
- 1 (dusra element)
- 2 (teesra element)
- 3 (chautha element)
- 4 (paanchva element)

Isliye, hum **len(toys) - 1** ka istemaal karte hain taaki humein sahi aur valid index mil sake.

## random password

### Define the character pool

- Create a string containing:
- Uppercase letters (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
- Lowercase letters (abcdefghijklmnopqrstuvwxyz)
- Digits (0123456789)

- You can use Python's string module (string.ascii_letters and string.digits) to get these.

## What is variable scope?

Variable scope is like the rooms where you play with your toys. Each room (function) has its own special toys (variables) that you can play with. What happens to a toy in one room doesn't affect the toy in another room.

###In this program:

- num_sides is a toy that you can see from both rooms, so you can play with it in both rooms.
- die_1 and die_2 are toys that you can only see in Room 2 (roll_dice() function), so you can only play with them in that room.

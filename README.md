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

In Python, the // operator is used for integer division, also known as floor division.

It divides the dividend (the number being divided) by the divisor (the number by which we are dividing) and returns the largest possible integer.

For example:
10 // 3 returns 3, not 3.33
7 // 2 returns 3, not 3.5

This is different from the / operator, which performs floating-point division and returns a decimal result.
For example:
10 / 3 returns 3.33
7 / 2 returns 3.5
So, in summary:

- / performs floating-point division
- // performs integer division (floor division)

## Return Statement in Python

Return statement ka kaam hai function se bahar nikalne ke liye. Jab hum return statement ko use karte hain, toh function ka execution ruk jata hai aur function se bahar nikalne ke liye jo value hum return statement ke saath dete hain, woh value function ko call karne wale code mein wapas aa jati hai.

Is example mein, add_many_numbers function mein return statement ka use karke hum total variable ki value ko wapas kar rahe hain. Phir, yeh value main function mein sum_of_many_number variable mein store ho jati hai.

Yeh return statement ka kaam hai:

- Function ka execution rukna
- Function se bahar nikalne ke liye value wapas karna

**Agar hum return statement ko use na karein, toh function ka execution poora hoga, lekin humein function se bahar nikalne ke liye koi value nahi milegi.**

## Function / Class Purpose

- tk.Tk() Creates the main application window
- tk.Canvas() Creates a drawing area (the canvas)
- canvas.pack() Places the canvas into the window
- canvas.create_rectangle(x1, y1, x2, y2, \*\*options) Draws a rectangle on the canvas
- canvas.itemconfig(id, fill='color') Changes the color of an existing item
- canvas.bind(event, handler) Attaches mouse or key events to functions

### creating eraser

## Make a Draggable Eraser
**Imagine a little rectangle on the screen that you can move around with your mouse. As it moves, it “erases” the blue cells it touches by turning them white.**

### **Why is mainloop() needed?**
- root.mainloop() starts the Tkinter event loop.
- Without it, the script runs and exits instantly, so the window doesn't stay open.

Pack function ke kaam
### Pack function ke kaam mein shamil hain:

- Widgets ko window mein add karna: Pack function widgets ko window mein add karta hai.
- Widgets ko arrange karna: Pack function widgets ko ek dusre ke neeche ya saath mein arrange karta hai.
- Widgets ko resize karna: Pack function widgets ko window ke size ke hisab se resize karta hai.
- Widgets ko position karna: Pack function widgets ko window mein ek specific position par position karta hai.

## Create a rectangle with a tag
rect = canvas.create_rectangle(10, 10, 50, 50, tags="cell")

### Use the tag to move the rectangle
canvas.move("cell", 10, 10)

### Use the tag to delete the rectangle
canvas.delete("cell")

- r1["x2"] < r2["x1"]: This condition checks if the right edge of the first rectangle is to the left of the left edge of the second rectangle. If this is true, the rectangles do not overlap.
- r1["x1"] > r2["x2"]: This condition checks if the left edge of the first rectangle is to the right of the right edge of the second rectangle. If this is true, the rectangles do not overlap.
- r1["y2"] < r2["y1"]: This condition checks if the bottom edge of the first rectangle is above the top edge of the second rectangle. If this is true, the rectangles do not overlap.
- r1["y1"] > r2["y2"]: This condition checks if the top edge of the first rectangle is below the bottom edge of the second rectangle. If this is true, the rectangles do not overlap.
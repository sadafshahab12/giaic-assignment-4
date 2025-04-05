# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

root = tk.Tk()
root.title("Canvas Eraser")

# create canvas inside the window
canvas = tk.Canvas(root, width=500, height=500, bg="blue")
canvas.pack()


# grid size
rows = 10
cols = 10
cell_size = 50  # 500/10 = 50

cells = []

for row in range(rows):
    for col in range(cols):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        rect = canvas.create_rectangle(
            x1, y1, x2, y2, fill="blue", outline="white", tags="cell"
        )
        # storing the cell info in a cell list
        cells.append({"id": rect, "x1": x1, "y1": y1, "x2": x2, "y2": y2})
root.mainloop()

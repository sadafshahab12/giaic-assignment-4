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

# create eraser rectangle

eraser_rect = None  # it will store the eraser rectangle id
eraser_overlap = None


def is_overlapping(r1, r2):
    """function to check if two rectangles overlap"""
    return not (
        r1["x2"] < r2["x1"]
        or r1["x1"] > r2["x2"]
        or r1["y2"] < r2["y1"]
        or r1["y1"] > r2["y2"]
        # This takes two rectangles: r1 and r2 (with x1, y1, x2, y2), and returns True if they overlap.
    )


def on_mouse_down(event):
    global eraser_rect
    x, y = event.x, event.y
    eraser_size = 30
    eraser_rect = canvas.create_rectangle(
        x, y, x + eraser_size, y + eraser_size, outline="black", width=2
    )


def on_mouse_drag(event):
    """function for eraser to follow mouse movement and drag"""
    global eraser_rect, eraser_overlap
    if eraser_rect:
        eraser_size = 30
        x, y = event.x, event.y
        canvas.coords(eraser_rect, x, y, x + eraser_size, y + eraser_size)

        eraser_overlap = {
            "x1": x,
            "y1": y,
            "x2": x + eraser_size,
            "y2": y + eraser_size,
        }

        for cell in cells:
            if is_overlapping(eraser_overlap, cell):
                canvas.itemconfig(cell["id"], fill="white")


def on_mouse_release(event):
    """function to remove the eraser after releasing the mouse"""
    global eraser_rect, eraser_overlap
    if eraser_rect:
        canvas.delete(eraser_rect)
        eraser_rect = None
        eraser_overlap = None


canvas.bind(
    "<Button-1>", on_mouse_down
)  # when mouse i clicked, create eraser rectangle
canvas.bind(
    "<B1-Motion>", on_mouse_drag
)  # when mouse is dragged, move the eraser rectangle
canvas.bind("<ButtonRelease-1>", on_mouse_release)


root.mainloop()

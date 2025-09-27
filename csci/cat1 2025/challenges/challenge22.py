"""
Challenge 22

2D array with coloured backgrounds based on the colour
"""

## MODULES
import tkinter as tk # gui instead of console
import random

## MAIN
root = tk.Tk()
root.title("Grid")

# array
rows = 10
cols = 10

array = [[random.randint(0, 15) for _ in range(cols)] for _ in range(rows)] # random numbers

# colour map
colours = ['#%02x%02x%02x' % (i*17, i*17, i*17) for i in range(16)]

# array display
for i in range(rows):
    for j in range(cols):
        num = array[i][j]
        label = tk.Label(root, text=str(num), width=4, height=2, bg=colours[num])
        label.grid(row=i, column=j)

root.mainloop()

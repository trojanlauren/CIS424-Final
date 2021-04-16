import tkinter as tk
from tkinter import *
from graphics import Graphics

# create window
root = tk.Tk()
root.title("Calculator")

graphics = Graphics()

graphics.BuildWindow(root)

# create loop to detect events
root.mainloop()
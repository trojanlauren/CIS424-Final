import tkinter as tk
from tkinter import *
import graphics

# create window
root = tk.Tk()
root.title("Calculator")

graphics.BuildWindow(root)

# create loop to detect events
root.mainloop()
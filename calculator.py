import tkinter as tk
from tkinter import *

# create window
root = tk.Tk()
root.title("Calculator")

#label to display output
lblOutput = Label(root, text = "Test").grid(row=0, column = 0)

# declare + display buttons
# numbers
btn1 = Button(root, text = "1", width=2).grid(row=4,column=0)
btn2 = Button(root, text = "2", width=2).grid(row=4,column=1)
btn3 = Button(root, text = "3", width=2).grid(row=4,column=2)
btn4 = Button(root, text = "4", width=2).grid(row=3,column=0)
btn5 = Button(root, text = "5", width=2).grid(row=3,column=1)
btn6 = Button(root, text = "6", width=2).grid(row=3,column=2)
btn7 = Button(root, text = "7", width=2).grid(row=2,column=0)
btn8 = Button(root, text = "8", width=2).grid(row=2,column=1)
btn9 = Button(root, text = "9", width=2).grid(row=2,column=2)
btn0 = Button(root, text = "0", width=2).grid(row=5,column=0)

# functions
btnLog = Button(root, text = "log", width=2).grid(row=4,column=4)
btnPi = Button(root, text = "pi", width=2).grid(row=5,column=4)
btnSin = Button(root, text = "sin", width=2).grid(row=1,column=4)
btnCos = Button(root, text = "cos", width=2).grid(row=2,column=4)
btnTan = Button(root, text = "tan", width=2).grid(row=3,column=4)

# operators
btnDec = Button(root, text = ".", width=2).grid(row=5,column=1)
btnEq = Button(root, text = "=", width=2).grid(row=5,column=3)
btnAdd = Button(root, text = "+", width=2).grid(row=4,column=3)
btnSub = Button(root, text = "-", width=2).grid(row=3,column=3)
btnMult = Button(root, text = "X", width=2).grid(row=2,column=3)
btnDiv = Button(root, text = "/", width=2).grid(row=1,column=3)
btnNeg = Button(root, text = "(-)", width=2).grid(row=1,column=1)
btnMod = Button(root, text = "%", width=2).grid(row=1,column=0)
btnSqrt = Button(root, text = "Sq", width=2).grid(row=1,column=2)
btnDel = Button(root, text = "C", width=2).grid(row=5,column=2)
btnClr = Button(root, text = "AC", width=2).grid(row=1,column=0)

# create loop to detect events
root.mainloop()




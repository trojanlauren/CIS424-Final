import tkinter as tk
from tkinter import *
import mathFunctions

def BuildWindow(root):
    width = 320
    height = 443

    #label to display output
    lblOutput = Label(root, text = "Test", width = 10, height = 3).grid(row = 0, column = 0)

    # declare + display buttons
    # numbers
    btn1 = CreateButton(root, text = "1", width = 10, height = 3, row = 6, column = 0, function = hello)
    btn2 = CreateButton(root, text = "2", width = 10, height = 3, row = 6, column = 1, function = hello)
    btn3 = CreateButton(root, text = "3", width = 10, height = 3, row = 6, column = 2, function = hello)
    btn4 = CreateButton(root, text = "4", width = 10, height = 3, row = 5, column = 0, function = hello)
    btn5 = CreateButton(root, text = "5", width = 10, height = 3, row = 5, column = 1, function = hello)
    btn6 = CreateButton(root, text = "6", width = 10, height = 3, row = 5, column = 2, function = hello)
    btn7 = CreateButton(root, text = "7", width = 10, height = 3, row = 4, column = 0, function = hello)
    btn8 = CreateButton(root, text = "8", width = 10, height = 3, row = 4, column = 1, function = hello)
    btn9 = CreateButton(root, text = "9", width = 10, height = 3, row = 4, column = 2, function = hello)
    btn0 = CreateButton(root, text = "0", width = 10, height = 3, row = 7, column =  1, function = hello)

    # functions
    btnLog = CreateButton(root, text = "log", width = 10, height = 3, row = 1, column = 0, function = hello)
    btnPi = CreateButton(root, text = "π", width = 10, height = 3, row = 1, column = 1, function = hello)
    btnE = CreateButton(root, text = "e", width = 10, height = 3, row = 2, column = 0, function = hello)
    btnSin = CreateButton(root, text = "sin", width = 10, height = 3, row = 2, column = 1, function = hello)
    btnCos = CreateButton(root, text = "cos", width = 10, height = 3, row = 2, column = 2, function = hello)
    
    btnTan = CreateButton(root, text = "tan", width = 10, height = 3, row = 2, column = 3, function = hello)

    # operators
    btnDec = CreateButton(root, text = ".", width = 10, height = 3, row = 7, column = 2, function = hello)

    btnEq = CreateButton(root, text = "=", width = 10, height = 3, row = 7, column = 3, function = hello)
    btnAdd = CreateButton(root, text = "+", width = 10, height = 3, row = 6, column = 3, function = hello)
    btnSub = CreateButton(root, text = "-", width = 10, height = 3, row = 5, column = 3, function = hello)
    btnMult = CreateButton(root, text = "X", width = 10, height = 3, row = 4, column = 3, function = hello)
    btnDiv = CreateButton(root, text = "/", width = 10, height = 3, row = 3, column = 3, function = hello)
    btnNeg = CreateButton(root, text = "(-)", width = 10, height = 3, row = 7, column = 0, function = hello)
    btnMod = CreateButton(root, text = "%", width = 10, height = 3, row = 3, column = 0, function = hello)
    btnSquare = CreateButton(root, text = "x²", width = 10, height = 3, row = 3, column = 1, function = hello)
    btnSqrt = CreateButton(root, text = "Sq", width = 10, height = 3, row = 3, column = 2, function = hello)
    btnDel = CreateButton(root, text = "Del", width = 10, height = 3, row = 1, column = 3, function = hello)
    btnClr = CreateButton(root, text = "C", width = 10, height = 3, row = 1, column = 2, function = hello)
    
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()
    x = (widthScreen / 2) - (width / 2)
    y = (heightScreen / 2) - ( height / 2 ) - ( height / 4 )

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def hello(event):
    print("hello")

def CreateButton(root, text, width, height, row, column, function):
    btn = Button(root, text = text, width = width, height = height)
    btn.grid(row = row, column = column)
    btn.bind('<Button-1>', func=function)
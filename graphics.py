import tkinter as tk
from tkinter import *
from CalcState import CalcState

class Graphics:

	def __init__(self):
		self.CalcState = None
	
	def BuildWindow(self, root):
		width = 320
		height = 502

		#label to display output
		lblOutput = Label(root, text = "0", height = 2, font=("Arial", 16))
		lblOutput.grid(row = 0, column = 0, columnspan = 4)		

		# declare + display buttons
		# numbers
		btn1 = self.CreateButton(root, text = "1", width = 10, height = 3, row = 7, column = 0, function = self.TypeButton)
		btn2 = self.CreateButton(root, text = "2", width = 10, height = 3, row = 7, column = 1, function = self.TypeButton)
		btn3 = self.CreateButton(root, text = "3", width = 10, height = 3, row = 7, column = 2, function = self.TypeButton)
		btn4 = self.CreateButton(root, text = "4", width = 10, height = 3, row = 6, column = 0, function = self.TypeButton)
		btn5 = self.CreateButton(root, text = "5", width = 10, height = 3, row = 6, column = 1, function = self.TypeButton)
		btn6 = self.CreateButton(root, text = "6", width = 10, height = 3, row = 6, column = 2, function = self.TypeButton)
		btn7 = self.CreateButton(root, text = "7", width = 10, height = 3, row = 5, column = 0, function = self.TypeButton)
		btn8 = self.CreateButton(root, text = "8", width = 10, height = 3, row = 5, column = 1, function = self.TypeButton)
		btn9 = self.CreateButton(root, text = "9", width = 10, height = 3, row = 5, column = 2, function = self.TypeButton)
		btn0 = self.CreateButton(root, text = "0", width = 10, height = 3, row = 8, column =  1, function = self.TypeButton)

		# functions
		btnLog = self.CreateButton(root, text = "log", width = 10, height = 3, row = 2, column = 0, function = self.TypeButton)
		btnPi = self.CreateButton(root, text = "π", width = 10, height = 3, row = 1, column = 1, function = self.TypeButton)
		btnE = self.CreateButton(root, text = "e", width = 10, height = 3, row = 1, column = 0, function = self.TypeButton)
		btnSin = self.CreateButton(root, text = "sin", width = 10, height = 3, row = 2, column = 1, function = self.TypeButton)
		btnCos = self.CreateButton(root, text = "cos", width = 10, height = 3, row = 2, column = 2, function = self.TypeButton)
		btnTan = self.CreateButton(root, text = "tan", width = 10, height = 3, row = 2, column = 3, function = self.TypeButton)

		# operators
		btnDec = self.CreateButton(root, text = ".", width = 10, height = 3, row = 8, column = 2, function = self.TypeButton)
		btnEq = self.CreateButton(root, text = "=", width = 10, height = 3, row = 8, column = 3, function = self.EvaluateCalcString)
		btnAdd = self.CreateButton(root, text = "+", width = 10, height = 3, row = 7, column = 3, function = self.TypeButton)
		btnSub = self.CreateButton(root, text = "-", width = 10, height = 3, row = 6, column = 3, function = self.TypeButton)
		btnMult = self.CreateButton(root, text = "*", width = 10, height = 3, row = 5, column = 3, function = self.TypeButton)
		btnDiv = self.CreateButton(root, text = "/", width = 10, height = 3, row = 4, column = 3, function = self.TypeButton)
		btnNeg = self.CreateButton(root, text = "(+/-)", width = 10, height = 3, row = 8, column = 0, function = self.AddNegation)
		btnLn = self.CreateButton(root, text = "ln", width = 10, height = 3, row = 3, column = 0, function = self.TypeButton)
		btnMod = self.CreateButton(root, text = "mod", width = 10, height = 3, row = 3, column = 1, function = self.TypeButton)
		btnSquare = self.CreateButton(root, text = "x²", width = 10, height = 3, row = 3, column = 2, function = self.TypeButton)
		btnSqrt = self.CreateButton(root, text = "Sqrt", width = 10, height = 3, row = 3, column = 3, function = self.TypeButton)
		btnDel = self.CreateButton(root, text = "Del", width = 10, height = 3, row = 1, column = 3, function = self.DeleteLast)
		btnClr = self.CreateButton(root, text = "C", width = 10, height = 3, row = 1, column = 2, function = self.ClearScreen)
		btnLeftPar = self.CreateButton(root, text = "(", width = 10, height = 3, row = 4, column = 0, function = self.TypeButton)
		btnRightPar = self.CreateButton(root, text = ")", width = 10, height = 3, row = 4, column = 1, function = self.TypeButton)
		btnFact = self.CreateButton(root, text = "!", width = 10, height = 3, row = 4, column = 2, function = self.TypeButton)

		widthScreen = root.winfo_screenwidth()
		heightScreen = root.winfo_screenheight()
		x = (widthScreen / 2) - (width / 2)
		y = (heightScreen / 2) - ( height / 2 ) - ( height / 4 )

		root.geometry('%dx%d+%d+%d' % (width, height, x, y))
		
		self.CalcState = CalcState(lblOutput)
		
	def TypeButton(self, event):
		self.CalcState.AddOutputLabelText(event.widget['text'])
		
	def EvaluateCalcString(self, event):
		self.CalcState.CalculateResult()	

	def ClearScreen(self, event):
		self.CalcState.ClearText()

	def DeleteLast(self, event):
		self.CalcState.RemoveLast()	

	def AddNegation(self, event):
		self.CalcState.AddNegation()

	def CreateButton(self, root, text, width, height, row, column, function):
		btn = Button(root, text = text, width = width, height = height)
		btn.grid(row = row, column = column)
		btn.bind('<Button-1>', func=function)

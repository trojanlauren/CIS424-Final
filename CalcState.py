import tkinter as tk
from tkinter import *
import math

class CalcState:
	def __init__(self, outputLabel):		
		self.OutputLabel = outputLabel
		self.ShouldReset = True		
		self.EqualReset = False
		self.LastValue = ''
		
	def SetShouldReset(self, value = True):
		self.ShouldReset = value

	def RemoveLast(self):
		text = self.OutputLabel['text']
		if len(text) == 1:
			self.OutputLabel['text'] = '0'
			return
		else:
			toRemove = text[-1]
			if (toRemove == ' '):
				self.OutputLabel['text'] = text[:-2]
			else:
				self.OutputLabel['text'] = text[:-1]

	def ClearText(self):
		self.OutputLabel['text'] = '0'
		self.SetShouldReset()
		self.EqualReset = False

	def AddOutputLabelText(self, text):
		if (self.ShouldReset):
			if text == ".":
				self.OutputLabel = "0."
			elif self.IsOperator(text):
				self.OutputLabel['text'] = "0 " + text
			else:
				self.OutputLabel['text'] = text

			self.SetShouldReset(False)
			self.EqualReset = False
			self.LastValue = text
		else:
			isOperator = self.IsOperator(text)
			isNumericOrDecimal = self.IsTextNumericOrDecimal(text)
		
			if (isNumericOrDecimal and self.EqualReset == True):
				self.OutputLabel['text'] = text 
			else:
				currLabelText = self.OutputLabel['text']
				space = ' '
			
				if (isNumericOrDecimal and self.IsTextNumericOrDecimal(currLabelText[-1])):
					space = ''

				if isOperator and self.IsOperator(self.LastValue):
					undoLength = len(self.LastValue) * -1
					currLabelText = currLabelText[:undoLength]
					space = ''

				if text == '.' and self.IsOperator(self.LastValue):
					text = "0."
			
				self.OutputLabel['text'] = currLabelText + space + text 
			
			self.EqualReset = False
			
			self.LastValue = text
			
	def CalculateResult(self):
		text = self.OutputLabel['text'].replace(' ', '')
		text = self.ReplaceSymbols(text)
		
		try:
			text = str(eval(text))
		except:
			text = "Invalid Expression"
			self.SetShouldReset(True)
		
		self.OutputLabel['text'] = text
		self.EqualReset = True
	
	def ReplaceSymbols(self, text):
		text = text.replace('π', 'math.pi').replace('e', 'math.e').replace('sin', 'math.sin')
		text = text.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
		
		return text
		
	def IsTextNumericOrDecimal(self, text):
		return (self.IsNum(text) or text == '.')

	def IsOperator(self, text):
		if text == '/' or text == '*' or text == '-' or text == '+':
			return True
		else:
			return False

	def AddNegation(self):
		currLabelText = self.OutputLabel['text']

		if self.IsTextNumericOrDecimal(self.LastValue):
			oldValText = self.OutputLabel['text'].split(' ')[-1]
			newVal = 0
			try:
				newVal = int(oldValText)
			except:
				newVal = float(oldValText)

			newVal *= -1
			undoLength = len(oldValText) * -1
			currLabelText = currLabelText[:undoLength] + str(newVal)

			self.OutputLabel['text'] = currLabelText

			self.LastValue = str(newVal)

	def IsNum(self, text):
		try:
			float(text)
		except:
			return False
		else:
			return True
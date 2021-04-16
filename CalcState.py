import tkinter as tk
from tkinter import *
import math

class CalcState:
	def __init__(self, outputLabel):		
		self.OutputLabel = outputLabel
		self.ShouldReset = True		
		self.EqualReset = False
		
	def SetShouldReset(self, value = True):
		self.ShouldReset = value
		
	def AddOutputLabelText(self, text):
		if (self.ShouldReset):
			self.OutputLabel['text'] = text
			self.SetShouldReset(False)
		else:
			numericOrDecimal = self.IsTextNumericOrDecimal(text)
		
			if (numericOrDecimal and self.EqualReset == True):
				self.OutputLabel['text'] = text 
			else:
				currLabelText = self.OutputLabel['text']
				space = ' '
			
				if (numericOrDecimal and len(currLabelText) > 0 and self.IsTextNumericOrDecimal(currLabelText[-1])):
					space = ''
			
				self.OutputLabel['text'] = currLabelText + space + text 
			
			self.EqualReset = False
			
	def CalculateResult(self):
		text = self.OutputLabel['text'].replace(' ', '')
		text = self.ReplaceSymbols(text)
		
		text = str(eval(text))
		
		self.OutputLabel['text'] = text
		self.EqualReset = True
	
	def ReplaceSymbols(self, text):
		text = text.replace('π', 'math.pi').replace('e', 'math.e').replace('sin', 'math.sin')
		text = text.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
		
		return text
		
	def IsTextNumericOrDecimal(self, text):
		return (text.isnumeric() or text == '.')
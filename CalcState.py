import tkinter as tk
from tkinter import *
import math

class CalcState:
	def __init__(self, outputLabel):		
		self.OutputLabel = outputLabel
		self.ShouldReset = True		
		self.PartialReset = False
		self.LastValue = ''
		
	def SetShouldReset(self, value = True):
		self.ShouldReset = value

	def RemoveLast(self):
		text = self.OutputLabel['text']
		if len(text) == 1:
			self.OutputLabel['text'] = '0'
			self.SetShouldReset()
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
		self.PartialReset = False

	def AddOutputLabelText(self, text):
		if text == 'x²':
			text = '²'
		if text == '!':
			text = 'fact'

		if (self.ShouldReset):
			if text == ".":
				self.OutputLabel = "0."
			elif self.IsOperator(text):
				self.OutputLabel['text'] = "0 " + text
			elif self.IsSpecialFunction(text):
				self.OutputLabel['text'] = text + "("
			else:
				self.OutputLabel['text'] = text

			self.SetShouldReset(False)
			self.PartialReset = False
			self.LastValue = text
		else:
			isOperator = self.IsOperator(text)
			isNumericOrDecimal = self.IsTextNumericOrDecimal(text)
			isSpecialFunction = self.IsSpecialFunction(text)

			if (isNumericOrDecimal and self.PartialReset == True):
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

				if text == '²':
					space = ''

				if isSpecialFunction:
					text += "("
					space = ''
					
					if self.PartialReset:
						currLabelText = text
						text = ''

				self.OutputLabel['text'] = currLabelText + space + text 
			
			self.PartialReset = False
			
			self.LastValue = text
			
	def CalculateResult(self):
		text = self.OutputLabel['text'].replace(' ', '')
		text = self.ReplaceSymbols(text)
		
		try:
			num = float(eval(text))
			if (num.is_integer()):
				num = int(num)

			text = str(num)
		except:
			text = "Invalid Expression"
			self.SetShouldReset(True)
		
		
		self.OutputLabel['text'] = text
		self.PartialReset = True
	
	def ReplaceSymbols(self, text):
		text = text.replace('π', 'math.pi').replace('e', 'math.e')
		text = text.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
		text = text.replace('ln', 'math.log').replace('log', 'math.log10').replace('Sq',  'math.sqrt')
		text = text.replace('mod', '%').replace('²', '**2').replace('fact' , 'math.factorial')
		text = text.replace('(-)', '(-1)*')
		
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
		return (text.isnumeric() or text == '.')


	def IsSpecialFunction(self, text):
		text = text.lower()
		if ( text == "sin" or text == "cos" or text == "tan" 
			or text == "log" or text == "sq" or text == "ln" or text == "fact"):
			return True
		
		return False
	
	
	
	def calculator (Choice):
		
	if Choice == '+':
            Num_1 = int( input ( 'Enter first number: ' ))
            Num_2 = int (input (  'Enter second number: '))
            print('{} + {} = '.format(Num_1, Num_2))
            print(Num_1 + Num_2)
	
	 elif  Choice =="-":
            Num_1 = int( input ( 'Enter first number: ' ))
            Num_2 = int (input (  'Enter second number: '))
            print('{} - {} = '.format(Num_1, Num_2))
            print(Num_1 - Num_2)
		
		
	
        elif  Choice == '*':
            Num_1 = int( input ( 'Enter first number: ' ))
            Num_2 = int (input (  'Enter second number: '))
            print('{} * {} = '.format(Num_1, Num_2))
            print(Num_1 * Num_2)
		
		
	  elif Choice == '/':
            Num_1 = int( input ( 'Enter first number: ' ))
            Num_2 = int (input (  'Enter second number: '))
            print('{} / {} = '.format(Num_1, Num_2))
            print(Num_1 / Num_2)

        elif Choice == 'sqrt':
            number= float(input(" Please Enter any numeric Value : "))
            squareRoot = math.sqrt(number)
            print("The Square Root of a Given Number {0}  = {1}".format(number, squareRoot))
	
	
	 else:
            print('Error')
	
	
	
	

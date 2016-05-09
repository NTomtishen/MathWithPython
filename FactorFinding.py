from sympy import *

exprstr = raw_input('Enter the expression: ')
try:
	expr = sympify(exprstr)
	print factor(expr)
except SympifyError:
	print ("Invalid input")
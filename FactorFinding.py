from sympy import *

x = Symbol('x')
exprstr = raw_input('Enter the expression: ')
try:
	expr = sympify(exprstr)
	print factor(expr)
except SympifyError:
	print ("Invalid input")
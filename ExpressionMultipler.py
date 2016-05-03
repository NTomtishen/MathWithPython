from sympy import expand, sympify, Symbol
from sympy.core.sympify import SympifyError

x = Symbol('x')
y = Symbol('y')

def product(expr1, expr2):
	prod = expand(expr1*expr2)
	print(prod)

expr1 = raw_input('Enter the first expression: ')
expr2 = raw_input('Enter the second expression: ')

try:
	expr1 = sympify(expr1)
	expr2 = sympify(expr2)
except SympifyError:
	print('Invalid input')
else:
	product(expr1, expr2)
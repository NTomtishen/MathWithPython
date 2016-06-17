from sympy import *
from sympy.plotting import plot
import sys

exprstr = raw_input('Enter an expression in terms of x and y: ')

x = Symbol('x')
try:
	expr1 = sympify(exprstr)
except SympifyError:
	print ('Invalid input(s)')
	sys.exit("Exiting")

p = plot(expr1, legend = true, show = false)
p.show()

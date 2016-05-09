from sympy import *
from sympy.plotting import plot

expr1str = raw_input('Enter your first expression in terms of x and y: ')
expr2str = raw_input('Enter your second expression in terms of x and y: ')

x = Symbol('x')
try:
	expr1 = sympify(expr1str)
	expr2 = sympify(expr2str)
except SympifyError:
	print ('Invalid input(s)')

soln = solve((expr1, expr2), dict=True)
solnx = soln[0]
solny = expr1.subs({x:solnx[x]})
print (solnx, solny)

p = plot(expr1, expr2, legend = true, show = false)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()
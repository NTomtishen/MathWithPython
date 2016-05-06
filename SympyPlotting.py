from sympy.plotting import plot
from sympy import *
# p = plot((2*x+3), (x, -5, 5), title = 'A Line', xlabel = 'x', ylabel = '2x + 3')

x = Symbol('x')
p = plot(2*x+3, 3*x+1, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()

'''
def plot_expression(expr):
	solutions = (solve(expr, y))
	expr_y = solutions[0]
	plot(expr_y)


expr = raw_input('Enter your expression in terms of x and y: ')
x = Symbol('x')
y = Symbol('y')
try:
	expr = sympify(expr)
except SympifyError:
	print('Invalid input')
else:
	plot_expression(expr)
'''
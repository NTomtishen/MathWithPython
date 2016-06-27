from sympy import *
from sympy.plotting import plot

exprstrs = []

newexprwanted = true

x = Symbol('x')

while newexprwanted:
    temp = raw_input('Enter an expression to graph or enter "stop" to stop entering expressions: ')
    if temp.upper() == "STOP":
        newexprwanted = false
    else:
        try:
            expr = sympify(temp)
            exprstrs.append(expr)
        except SympifyError:
            print ('Invalid input(s)')

plot(*exprstrs, legend = true)

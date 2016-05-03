'''
x = 1
print x + x + 1
'''
from sympy import *
from sympy.core.sympify import SympifyError
'''
x = Symbol('x')
y = Symbol('y')

p = x ** 3 + 3 *x**2*y + 3*x*y**2 + y**3
factors = factor(p)
pprint(p)
res = p.subs({x:1, y:2})
print res
'''

'''
x = Symbol('x')
expr = input('Enter a mathematical expression: ')
expr = sympify(expr)
print expr
'''

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
expr = a*x*x + b*x + c
pprint(expr)

pprint(solve(expr, x, dict=True))
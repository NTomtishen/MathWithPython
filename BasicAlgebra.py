'''
x = 1
print x + x + 1
'''
from sympy import Symbol, expand, factor, pprint
x = Symbol('x')
y = Symbol('y')

p = x ** 3 + 3 *x**2*y + 3*x*y**2 + y**3
factors = factor(p)
pprint(p)
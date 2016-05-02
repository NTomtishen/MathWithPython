'''
x = 1
print x + x + 1
'''
from sympy import *
x = Symbol('x')
y = Symbol('y')

p = x ** 3 + 3 *x**2*y + 3*x*y**2 + y**3
factors = factor(p)
pprint(p)
res = p.subs({x:1, y:2})
print res
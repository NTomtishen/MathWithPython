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

'''
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
expr = a*x*x + b*x + c
pprint(expr)

pprint(solve(expr, x, dict=True))
'''

'''
s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')
expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr,t, dict=True)
pprint(t_expr)
'''

x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12
soln = solve((expr1, expr2), dict=True)
print soln
soln = soln[0]
print expr1.subs({x:soln[x], y:soln[y]})
print expr2.subs({x:soln[x], y:soln[y]})
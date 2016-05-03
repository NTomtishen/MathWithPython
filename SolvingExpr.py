from sympy import Symbol, solve
x = Symbol('x')
expr = x**2 + 6*x + 6
print solve(expr)
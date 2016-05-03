from sympy import solve, Symbol
x = Symbol('x')
expr = raw_input('Enter the Quadratic Equation to solve: ')
print solve(expr, dict=True)
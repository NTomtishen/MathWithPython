from sympy import *

# Method to solve polynomial inequalities
'''
x = Symbol('x')
ineq_obj = -x**2 + 4 < 0
lhs = ineq_obj.lhs
p = Poly(lhs, x)
rel = ineq_obj.rel_op
print solve_poly_inequality(p, rel)
'''

# Method to solve rational inequalities
x = Symbol('x')
ineq_obj = ((x-1)/(x+2)) > 0
lhs = ineq_obj.lhs
numer, denom = lhs.as_numer_denom()
p1 = Poly(numer)
p2 = Poly(denom)
rel = ineq_obj.rel_op
print solve_rational_inequalities([[((p1, p2), rel)]])
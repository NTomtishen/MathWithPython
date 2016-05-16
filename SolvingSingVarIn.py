from sympy import *

def isolve():
	x = Symbol('x')
	ineq = input('Enter your inequality: ')
	ineq = sympify(ineq)
	ineq_obj = ineq
	if ineq.is_polynomial():
		lhs = ineq_obj.lhs
		p = Poly(lhs, x)
		rel = ineq_obj.rel_op
		print solve_poly_inequality(p, rel)
	elif ineq.is_rational_function():
		lhs = ineq_obj.lhs
		numer, denom = lhs.as_numer_denom()
		p1 = Poly(numer)
		p2 = Poly(denom)
		rel = ineq_obj.rel_op
		print solve_rational_inequalities([[((p1, p2), rel)]])
	else:
		print solve_univariate_inequality(ineq_obj, x, relational = False)
isolve()
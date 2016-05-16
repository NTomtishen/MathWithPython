from sympy import FiniteSet
from fractions import Fraction
members = [2, 4, 6, Fraction(1, 5)]
s = FiniteSet(*members)
print s
print len(s)
print 4 in s
print 15 in s
for member in s:
	print member
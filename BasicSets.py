from sympy import FiniteSet
from fractions import Fraction
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6, 8)
p = s**3
for elem in p:
	print elem
from sympy import *
n = Symbol('n')
nth = raw_input('Enter the nth term: ')
num = input('Enter the number of terms: ')
nth = sympify(nth)
s = summation(nth, (n, 1, num))
pprint(s)
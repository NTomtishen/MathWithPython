from fractions import Fraction
# Waits for user to type something then stores it as a
# Stores input as a string
a = input()
print a

# Converts a to an int or a float respectively.
# int(a) won't accept an a that is a float i.e 2.0 or a fractional number (3/4)
print int(a) + 1
print float(a) + 1

# Executes the try block unless there is a Value Error then it goes to the except block
try:
	a = float(input('Enter a number: '))
	print a
except ValueError:
	print('You entered an invalid number')

# Converts the input to int immediately
a = int(input())
print a
print a + 1

# .is_interger() returns true for floating point numbers if the number ends with .0
print 1.1.is_integer()
print 1.0.is_integer()

# Asks for a fraction then converts it to a Fraction object
a = Fraction(input('Enter a fraction: '))

# Will return invalid fraction for x/0 fractions
try:
	a = Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
	print ('Invalid fraction')

# Will convert a string like 2+3j into a complex number
try:
	z = complex(input('Enter a complex number: '))
except ValueError:
	print('Invalid complex number!')
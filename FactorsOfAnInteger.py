# A function that looks if a is a factor of b then returns True or False
def is_factor(a, b):
	if b % a == 0:
		return True
	else:
		return False

# A function that prints all positive factors of b
def factors(b):
	for i in range(1, b+1):
		if b % i == 0:
			print(i)

a = input('Enter your first number: ')
b = input('Enter the second number: ')
a = float(a)
b = float(b)

print is_factor(a, b)

'''
if b > 0 and b.is_integer():
	factors(int(b))
else:
	print('Please enter a positive integer')
'''
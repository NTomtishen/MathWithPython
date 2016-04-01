# A function that looks if a is a factor of b then returns True or False
def is_factor(a, b):
	if b % a == 0:
		return True
	else:
		return False

print 'Is 4 a factor of 1024?',
print is_factor(4, 1024)
print 'Is 322 a facor of 50134435?',
print is_factor(322, 50134435)

# A function that prints all positive factors of b
def factors(b):
	for i in range(1, b+1):
		if b % i == 0:
			print(i)

b = input('Your Number Please: ')
b = float(b)

if b > 0 and b.is_integer():
	factors(int(b))
else:
	print('Please enter a positive integer')
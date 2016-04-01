def is_factor(a, b):
	if b % a == 0:
		return True
	else:
		return False

print 'Is 4 a factor of 1024?',
print is_factor(4, 1024)
print 'Is 322 a facor of 50134435?', 
print is_factor(322, 50134435)
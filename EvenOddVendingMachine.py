while True:
	num = float(input('Please enter a number: '))
	if num.is_integer():
		num = int(num)
		if num % 2 == 0:	
			print 'The number you gave is even.'
			for item in range(10):
				print num + item*2
		if num % 2 != 0:
			print 'The number you gave is odd.'
			for item in range(10):
				print num + item*2
	else:
		print 'You entered an invalid number'
	answer = raw_input('Would you like to exit? (y) for yes ')
	if answer == 'y':
		break
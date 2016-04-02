def multi_table(a, b):
	for i in range(1, b+1):
		print('{0} x {1} = {2}'.format(a, i, a*i))

a = input('Enter a number: ')
b = input('Enter how many multiples you want: ')
multi_table(float(a), int(b))
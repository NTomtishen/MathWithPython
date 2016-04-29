from collections import Counter

def calculate_mean(numbers):
	s = float(sum(numbers))
	l = float(len(numbers))
	return s/l
'''
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
mean = calculate_mean(donations)
N = len(donations)
print('Mean donation over the last {0} days is {1}'.format(N, mean))
'''

def calculate_median(numbers):
	l = len(numbers)
	numbers.sort()

	if l % 2 == 0:
		m1 = l/2
		m2 = (l/2) + 1
		m1 = int(m1) - 1
		m2 = int(m2) - 1
		median = (numbers[m1] + numbers[m2])/2
	else:
		m = (l+1)/2
		m = int(m) - 1
		median = numbers[m]
	return median

'''
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
median = calculate_median(donations)
N = len(donations)
print('Median donation over the last {0} days is {1}'.format(N, median))
'''

def calculate_mode(numbers):
	c = Counter(numbers)
	numbers_freq = c.most_common()
	max_count = numbers_freq[0][1]

	modes = []
	for num in numbers_freq:
		if num[1] == max_count:
			modes.append(num[0])
	return modes

'''
scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
modes = calculate_mode(scores)
print('The mode(s) of the list of numbers are:')
for mode in modes:
	print(mode)
'''

def frequency_table(numbers):
	table = Counter(numbers)
	print ('Number\tFrequency')
	numbers_freq = table.most_common()
	numbers_freq.sort()
	print numbers_freq
	for number in numbers_freq:
		print ('{0}\t{1}'.format(number[0], number[1]))

'''
scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
frequency_table(scores)
'''

def find_range(numbers):
	lowest = min(numbers)
	highest = max(numbers)
	r = highest - lowest

	return lowest, highest, r

'''
donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
lowest, highest, r = find_range(donations)
print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))
'''

def find_differences(numbers):
	mean = calculate_mean(numbers)
	diff = []
	for num in numbers:
		diff.append(num - mean)
	return diff

def calculate_variance(numbers):
	diff = find_differences(numbers)
	squared_diff = []
	for d in diff:
		squared_diff.append(d ** 2)
	sum_squared_diff = sum(squared_diff)
	variance = sum_squared_diff/len(numbers)
	return variance

'''
donations = [382, 389, 377, 397, 396, 368, 369, 392, 398, 367, 393, 396]
variance = calculate_variance(donations)
print('The variance of the list of numbers is {0}'.format(variance))
std = variance ** 0.5
print('The standard deviation of the list of numbers is {0}'.format(std))
'''

def find_corr_x_y(x, y):
	n = len(x)
	prod = []
	for xi, yi in zip(x, y):
		prod.append(xi*yi)
	sum_prod_x_y = sum(prod)
	sum_x = sum(x)
	sum_y = sum(y)
	squared_sum_x = sum_x ** 2
	squared_sum_y = sum_y ** 2
	x_square = []
	for xi in x:
		x_square.append(xi ** 2)
	x_square_sum = sum(x_square)
	y_square = []
	for yi in y:
		y_square.append(yi ** 2)
	y_square_sum = sum(y_square)

	numerator = n*sum_prod_x_y - sum_x*sum_y
	denominator_term1 = n*x_square_sum - squared_sum_x
	denominator_term2 = n*y_square_sum - squared_sum_y
	denominator = (denominator_term1*denominator_term2)**0.5
	correlation = numerator/denominator
	return correlation
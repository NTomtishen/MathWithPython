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

scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
frequency_table(scores)
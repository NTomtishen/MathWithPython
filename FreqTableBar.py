import matplotlib.pyplot as plt
from collections import Counter

def print_frequency_table(numbers):
	table = Counter(numbers)
	numbers_freq = table.most_common()
	numbers_freq.sort()
	x_values = []
	y_values = []
	for number in numbers_freq:
		x_values.append(number[0])
		y_values.append(number[1])
	plt.bar(x_values, y_values)
	plt.title('Frequency Table')
	plt.xlabel('Number')
	plt.ylabel('Frequency')
	print plt.axis(xmax = 10, ymax = 6)
	plt.show()

scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
print_frequency_table(scores)
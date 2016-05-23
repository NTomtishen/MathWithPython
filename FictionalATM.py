import random

def get_index(probability):
	c_probability = 0
	sum_probability = []
	for p in probability:
		c_probability += p
		sum_probability.append(c_probability)
	r = random.random()
	for index, sp in enumerate(sum_probability):
		if r <= sp:
			return index
	return len(probability)-1

def dispense():
	dollar_bills = [5, 10, 20, 50]
	probability = [1.0/6.0, 1.0/6.0, 1.0/3.0, 1.0/3.0]
	bill_index = get_index(probability)
	return dollar_bills[bill_index]

five = 0.0
ten = 0.0
twenty = 0.0
fifty = 0.0
total = 0.0
for item in range(0, 1000000):
	bill = dispense()
	if bill == 5:
		five += 1
	elif bill == 10:
		ten += 1
	elif bill == 20:
		twenty += 1
	elif bill == 50:
		fifty += 1
	total += 1
print five/total, ten/total, twenty/total, fifty/total
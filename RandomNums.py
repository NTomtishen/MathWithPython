import random
'''
print random.randint(1, 6)
'''
print random.random()
'''
def toss():
	if random.random() < 2/3:
		return 0
	else:
		return 1

tails = 0
heads = 0
total = heads + tails
for item in range(0, 100):
	i = toss()
	if i == 1:
		tails += 1
	else:
		heads += 1
print tails, heads, total
'''
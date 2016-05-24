import random
trialnum = input('How many trials would you like to use? ')
total = 0.0
times = 0
for item in range(0, trialnum):
	times += 1
	total += random.randint(1, 6)
print "Expected value: 3.5"
print ('Trials: %s Trial average %s' % (times, total/times))
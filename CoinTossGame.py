import random
cash = input('Enter your starting amount: ')
times = 0
max = [cash, 0]
while cash > 0:
	# Heads is 1, Tails is 2
	coin = random.randint(1, 2)
	if coin == 1:
		cash += 1
		print 'Heads!',
	elif coin == 2:
		cash -= 1.5
		print 'Tails',
	print ('Current amount: %s' % (cash))
	times += 1
	if cash > max[0]:
		max[0] = cash
		max [1] = times
print 'Game Over! :( Current amount: %s. Coin tosses: %s' % (cash, times)
print 'You reached your max amount, %s, after %s toss(es)' % (max[0], max[1])
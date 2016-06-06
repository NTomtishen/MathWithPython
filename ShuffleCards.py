import random
x = range(1, 53)
random.shuffle(x)

cardnums = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

for item in x:
	if item <= 13:
		suit = 'Hearts'
	elif item <= 26:
		suit = 'Diamonds'
	elif item <= 39:
		suit = 'Clubs'
	else:
		suit = 'Spades'

	if suit == 'Hearts':
		num = cardnums[item - 1]
	elif suit == 'Diamonds':
		num = cardnums[item - 14]
	elif suit == 'Clubs':
		num = cardnums[item - 27]
	else:
		num = cardnums[item - 40]
	print num + ' of ' + suit
import random
import math

radius = input('Enter the desired radius: ')
x1 = radius
y1 = radius

def throwDarts(x):
	circlethrows = 0.0
	totalthrows = 0.0
	for item in range(0, x):
		x2 = random.uniform(0, 2*radius)
		y2 = random.uniform(0, 2*radius)

		distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

		if abs(distance) <= radius:
			circlethrows += 1
			totalthrows += 1
		else:
			totalthrows += 1
	square = 4 * radius**2
	circle = (circlethrows/totalthrows) * square
	return circle

area = math.pi * radius**2


print 'Radius: %s' % radius
estimate1 =  throwDarts(1000)
print 'Area: %s, Estimate (1000 darts): %s' % (area, estimate1)
estimate2 = throwDarts(100000)
print 'Area: %s, Estimate (100000 darts): %s' % (area, estimate2)
estimate3 = throwDarts(1000000)
print 'Area: %s, Estimate (1000000 darts): %s' % (area, estimate3)

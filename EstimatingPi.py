import random
import math

radius = 5
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
	return circle/square * 4

area = math.pi * radius**2

estimate1 =  throwDarts(10)
print 'Pi: %s, Estimate (10 darts): %s' % (math.pi, estimate1)
estimate2 =  throwDarts(100)
print 'Pi: %s, Estimate (100 darts): %s' % (math.pi, estimate2)
estimate3 = throwDarts(1000)
print 'Pi: %s, Estimate (1000 darts): %s' % (math.pi, estimate3)
estimate4 = throwDarts(10000)
print 'Pi: %s, Estimate (10000 darts): %s' % (math.pi, estimate4)
estimate5 = throwDarts(100000)
print 'Pi: %s, Estimate (100000 darts): %s' % (math.pi, estimate5)
estimate6 = throwDarts(1000000)
print 'Pi: %s, Estimate (1000000 darts): %s' % (math.pi, estimate6)
estimate7 = throwDarts(10000000)
print 'Pi: %s, Estimate (10000000 darts): %s' % (math.pi, estimate7)
import matplotlib.pyplot as plt

x_values = range(-10, 11)
y_values = []
for x in x_values:
	y = x**2 + 2*x + 1
	y_values.append(y)
plt.title('x^2 + 2x + 1')
plt.plot(x_values, y_values, marker = 'o')
plt.show()
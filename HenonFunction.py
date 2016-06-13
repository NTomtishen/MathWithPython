import matplotlib.pyplot as plt

def transform(p):
    x = p[0]
    y = p[1]
    x1 = y + 1 - 1.4 * x**2
    y1 = 0.3 * x
    return x1, y1

x = [0]
y = [0]
x1, y1 = 0, 0
for i in range(20000):
    x1, y1 = transform((x1, y1))
    x.append(x1)
    y.append(y1)
plt.plot(x, y, 'o')
plt.title("Henon's Function with 20,000 points")
plt.show()

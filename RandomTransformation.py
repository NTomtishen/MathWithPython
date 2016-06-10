import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x + 1, y - 1

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x + 1, y + 1

def transformation_3(p):
    x = p[0]
    y = p[1]
    return x - 1, y + 1

def transformation_4(p):
    x = p[0]
    y = p[1]
    return x - 1, y - 1

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    t = random.choice(transformations)
    x, y = t(p)
    return x, y

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

p = (0, 0)
n = int(input('Enter the number of iterations: '))
x, y = build_trajectory(p, n)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
ax = plt.axes()
ax.set_aspect('equal')
plt.show()

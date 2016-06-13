import random
import matplotlib.pyplot as plt

def transformation_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1

def transformation_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1

def transformation_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1

def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3]
    t = random.choice(transformations)
    x, y = t(p)
    return x, y

def draw_triangle(n):
    x = [0]
    y = [0]

    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

n = int(input('Enter the number of points in the Sierpinski Triangle: '))
x, y = draw_triangle(n)
plt.plot(x, y, 'o')
plt.title('Sierpinski Triangle with {0} points'.format(n))
plt.show()

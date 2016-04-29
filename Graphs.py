import matplotlib.pyplot as plt
import numpy as np

x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]
plt.plot(x_numbers, y_numbers, 'o')
print plt.xticks()
locs, labels = plt.xticks()
print locs
print labels
plt.xticks(np.arange(3), ('Test 1', 'Test 2'))
plt.show()
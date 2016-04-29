import matplotlib.pyplot as plt
import numpy as np

hourly_temp = [41, 41, 41, 44, 44, 45, 45, 46, 47, 47, 46, 45, 44, 44, 44]
hours = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
plt.title('Temperature in Ann Arbor over the course of a day')
plt.xlabel('Hour')
plt.ylabel('Temperature in F')
plt.plot(hours, hourly_temp, marker = 'o')
plt.xticks(np.arange(25), ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12AM'))
print plt.axis(xmin = 10, ymin = 0, ymax = 50)
plt.show()
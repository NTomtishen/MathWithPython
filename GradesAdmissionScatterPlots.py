import matplotlib.pyplot as plt
grades = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
admission = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
plt.scatter(grades, admission)
plt.xlabel('High school math grades')
plt.ylabel('College admission test scores')
plt.show()

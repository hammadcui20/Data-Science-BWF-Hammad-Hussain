import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 12]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()

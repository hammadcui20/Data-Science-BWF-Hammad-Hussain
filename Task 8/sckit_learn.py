from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 2, 5, 4])

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)
print("Predictions:", predictions)

plt.scatter(X, y, color='blue')
plt.plot(X, predictions, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()

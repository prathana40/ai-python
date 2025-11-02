import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,6,5,4,3,2,1])

# Scatter plot
plt.scatter(x, y, marker='+', color='black')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

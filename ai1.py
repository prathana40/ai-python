import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)    

plt.plot(x, 2*x + 1, 'r-', label='y=2x+1')   
plt.plot(x, 2*x + 2, 'g--', label='y=2x+2')  
plt.plot(x, 2*x + 3, 'b:', label='y=2x+3')   
plt.title("Lines y=2x+c")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.show()

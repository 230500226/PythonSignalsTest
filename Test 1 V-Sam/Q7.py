## Dealing with discrete functions, Best if we use numpy as it allows better array manipulation functions
import numpy as np
import matplotlib.pyplot as plt
# Time shifting Diagrams => At least the output entirely depends on the input, and the input depends on the previous input...
n = np.arange(-10, 10) # Create an array of numbers from -10 to 9, just integers
 #  -10, -9, -7, -6, -5, -4, -3, -2, -1,0, 1, 2, 3, 4, 5, 6, 7, 8, 9
x = [0, 0, 0, 0, 0,  0,  0,  -1, -1, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0]
# y[n] = 0.5*(x[n-3]+x[n])
y = 0.5*(np.roll(x, 3)+x)
indices = np.where((n >= -3) & (n <= 3))
print("The sum of the results is : ",np.sum(y[indices]))
# plt.stem(n, x) # Just to see if this graph is the same as the on epresented on the pdf
# plt.show()
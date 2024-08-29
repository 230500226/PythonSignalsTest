import numpy as np

n = np.arange(-5, 7)
x = [0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0]
h = [0, 0, -1, -1, 0, 1, 2, 3, 2, 1, 0, 0]
y = np.convolve(x, h, mode = "same")
Index = np.where(n == 1)
print(f"The convolution at y[{Index}] = {y[Index]}")
# print(y)
import numpy as np
import matplotlib.pyplot as plt

# Define two discrete sequences
n = np.arange(-6, 7)
x = np.array([0,0, 0, 0, 0, 0,0, 0, 2, 3, 2, 0,0])
h = np.array([0,0, 0, -1, -1, 0, 1, 2, 3, 2, 1, 0, 0])


# Perform convolution
y = np.convolve(x, h, mode='same')


plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.stem(n,x, basefmt=" ")  # Plots the x[n] function 
plt.title('Sequence x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.subplot(3, 1, 2)
plt.stem(n,h, basefmt=" ") # Plots the h[n] function 
plt.title('Sequence h[n]')
plt.xlabel('n')
plt.ylabel('h[n]')

plt.subplot(3, 1, 3)
plt.stem(n,y, basefmt=" ")
plt.title('Convolution y[n]') # Plots the convolution function 
plt.xlabel('n')
plt.ylabel('y[n]')

plt.tight_layout()
plt.show()

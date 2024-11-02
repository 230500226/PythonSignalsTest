import numpy as np
import matplotlib.pyplot as plt

# Ask the user to input the time points and values for the function x(t)
x_t_values = input("Enter the time points for the function x(t), separated by commas: ").split(',')
x_values = input("Enter the values for the function x(t) at these time points, separated by commas: ").split(',')

# Ask the user to input the time points and values for the function y(t)
y_t_values = input("Enter the time points for the function y(t), separated by commas: ").split(',')
y_values = input("Enter the values for the function y(t) at these time points, separated by commas: ").split(',')

# Ask the user to input the transformation parameters
A = float(input("Enter the amplitude scaling factor: "))  # amplitude scaling factor
B = float(input("Enter the amplitude shifting amount: "))  # amplitude shifting amount
C = float(input("Enter the time scaling factor: "))  # time scaling factor
D = float(input("Enter the time shifting units: "))  # time shifting units

# Convert the inputs to numpy arrays
x_t = np.array([float(value) for value in x_t_values])
x = np.array([float(value) for value in x_values])
y_t = np.array([float(value) for value in y_t_values])
y = np.array([float(value) for value in y_values])

# Apply the transformations to generate z(t)
z_t = C * (x_t)- D
z = A * x + B

# Plot x(t), y(t), and z(t)
plt.figure(figsize=(10, 6))

plt.fill_between(x_t, x, alpha=0.3, label='x(t)')
plt.fill_between(y_t, y, alpha=0.3, label='y(t)')
plt.fill_between(z_t, z, alpha=0.3, label='z(t)')

plt.xlabel('t')
plt.ylabel('Value')
plt.title('Functions x(t), y(t), and z(t)')
plt.legend()
plt.grid(True)
plt.show()
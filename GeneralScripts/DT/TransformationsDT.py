import numpy as np
import re

import matplotlib.pyplot as plt

# Ask the user to input the indices and corresponding values for the function x[n]
indices = input("Enter the indices for the function x[n], separated by commas: ").split(',')
values = input("Enter the corresponding values for the function x[n], separated by commas: ").split(',')

# Convert the inputs to numpy arrays
n = np.array([int(index) for index in indices])
x_n = np.array([float(value) for value in values])

# Print the input function values at the indices
print("Input function values at the indices:")
for index, value in zip(n, x_n):
    print(f"n = {index}: x[n] = {value}")

# Plot the original function x[n]
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.stem(n, x_n)
plt.title('Original function x[n]')

# Ask the user to input a transformation function
print("Enter a transformation function. Examples: '-n' for time reversal, 'n/2' for time scaling, 'n-2' for time shifting, 'n/2-3' for both time scaling and time shifting.")
transformation = input()

# Use regular expressions to identify the operations and their order
match = re.search(r'(-)?n(/(\d+))?((\+|-)(\d+))?', transformation)
neg_n = match.group(1) is not None
div_n = match.group(3)
shift_op = match.group(5)
shift_n = match.group(6)

# Apply the operations in the correct order
if neg_n:
    x_n = x_n[::-1]
if div_n:
    n = n / int(div_n)
if shift_op and shift_n:
    if shift_op == '+':
        n = n + int(shift_n)
    else:
        n = n - int(shift_n)

# Print the function values at the indices after transformation
print("Function values at the indices after transformation:")
for index, value in zip(n, x_n):
    print(f"n = {index}: y[n] = {value}")

# Plot the transformed function y[n]
plt.subplot(1, 2, 2)
plt.stem(n, x_n)
plt.xticks(n)  # Set the x-axis ticks
plt.yticks(x_n)  # Set the y-axis ticks
plt.title('Transformed function y[n]')

plt.show()
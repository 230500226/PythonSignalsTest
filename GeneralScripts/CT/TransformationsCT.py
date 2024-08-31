import numpy as np
import matplotlib.pyplot as plt
import re

# Ask the user to input the indices and corresponding values for the function x(t)
indices = input("Enter the indices for the function x(t), separated by commas: ").split(',')
values = input("Enter the corresponding values for the function x(t), separated by commas: ").split(',')

# Convert the inputs to numpy arrays
t = np.array([float(index) for index in indices])
x_t = np.array([float(value) for value in values])

# Print the input function values at the indices
print("Input function values at the indices:")
for index, value in zip(t, x_t):
    print(f"t = {index}: x(t) = {value}")

# Plot the original function x(t)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x_t)
plt.title('Original function x(t)')

# Ask the user to input a transformation function
print("Enter a transformation function. Examples: '-t' for time reversal, 't/2' for time scaling, 't-2' for time shifting, 't/2-3' for both time scaling and time shifting.")
transformation = input()

# Use regular expressions to identify the operations and their order
match = re.search(r'(-)?t(/(\d+))?((\+|-)(\d+))?', transformation)
neg_t = match.group(1) is not None
div_n = match.group(3)
shift_op = match.group(5)
shift_n = match.group(6)

# Apply the operations in the correct order
if neg_t:
    x_t = x_t[::-1]
if div_n:
    t = t / float(div_n)
if shift_op and shift_n:
    if shift_op == '+':
        t = t + float(shift_n)
    else:
        t = t - float(shift_n)

# Ask the user to input an amplitude scaling factor
amp_scale = float(input("Enter an amplitude scaling factor: "))

# Apply amplitude scaling
x_t = amp_scale * x_t

# Ask the user to input an amplitude shifting value
amp_shift = float(input("Enter an amplitude shifting value: "))

# Apply amplitude shifting
x_t = x_t + amp_shift

# Print the function values at the indices after transformation
print("Function values at the indices after transformation:")
for index, value in zip(t, x_t):
    print(f"t = {index}: y(t) = {value}")

# Plot the transformed function y(t)
plt.subplot(1, 2, 2)
plt.plot(t, x_t)
plt.xticks(t)  # Set the x-axis ticks
plt.yticks(x_t)  # Set the y-axis ticks
plt.title('Transformed function y(t)')

plt.show()
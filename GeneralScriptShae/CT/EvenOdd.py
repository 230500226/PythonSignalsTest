import sympy as sm
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# Define the actual symbol/ Variable
t = sm.Symbol('t')

# Define the Original Function
def input_piecewise():
    # Initialize the pieces list
    pieces = []

    # Initialize the previous index to negative infinity
    prev_index = -sm.oo

    # Define the symbol t
    t = sm.Symbol('t')

    # Ask the user for all indices
    indices = input("Enter all indices: ")
    indices = [sm.sympify(index) for index in indices.split(',')]

    # Ask the user for all values
    values = input("Enter the value for each index: ")
    values = [sm.sympify(value) for value in values.split(',')]

    # Loop over the indices and values
    for index, value in zip(indices, values):
        # Add the piece to the pieces list
        pieces.append((value, (prev_index <= t) & (t < index)))

        # Update the previous index
        prev_index = index

    # Add the default piece (0, True)
    pieces.append((0, t >= prev_index))

    # Create the Piecewise function
    equation = sm.Piecewise(*pieces)

    return equation, indices, values

# Test the function
equation, indices, values = input_piecewise()
print("The piecewise function is:", equation)

# Define the Flipped Function
flipped_equation = equation.subs(t, -t)

# Finding the Even Component
xeven = (equation + flipped_equation) / 2
xodd = (equation-flipped_equation) / 2
xeven_func = sm.lambdify(t, xeven, 'numpy') # Convert the even component to a lambda function for integration
xodd_func = sm.lambdify(t, xodd, 'numpy')
inter, miss = quad(xodd_func, -3, 3)
result, error = quad(xeven_func, -3, 3)
print("Integration even result:", result)
print("Integration odd result:", inter)

# Print the even and odd indices and their corresponding values
even_indices = [index for index in indices if index % 2 == 0]
odd_indices = [index for index in indices if index % 2 != 0]
even_values = [value for index, value in zip(indices, values) if index % 2 == 0]
odd_values = [value for index, value in zip(indices, values) if index % 2 != 0]
print("Even indices:", even_indices)
print("Odd indices:", odd_indices)
print("Values at even indices:", even_values)
print("Values at odd indices:", odd_values)

# Plot the original, even, and odd functions separately
x = np.linspace(-8, 8, 400)
y_original = np.array([float(equation.subs(t, val)) for val in x])
y_even = np.array([float(xeven.subs(t, val)) for val in x])
y_odd = np.array([float(xodd.subs(t, val)) for val in x])

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x, y_original, 'b-')
plt.title('Original Function')

plt.subplot(3, 1, 2)
plt.plot(x, y_even, 'g-')
plt.title('Even Function')

plt.subplot(3, 1, 3)
plt.plot(x, y_odd, 'r-')
plt.title('Odd Function')

plt.tight_layout()
plt.show()
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Heaviside or unit step function NOT WOKRING

# Print a statement explaining the notation
print("Please enter your formula. Use 'x' for the variable, 'u' for the Heaviside function, 'd' for the Dirac delta function, and '^' for exponentiation.")
print("For example, a valid function could be: (x-2)*u(x-2)")

# Ask the user for input of a formula
formula = input("Enter your formula: ")

# Replace u with Heaviside, d with DiracDelta and ^ with **
formula = formula.replace('u', 'Heaviside').replace('d', 'DiracDelta').replace('^', '**')

# Define the symbols
x = sp.symbols('x')

# Parse the formula
f = sp.sympify(formula, locals={'Heaviside': sp.Heaviside, 'DiracDelta': sp.DiracDelta})

# Create a range of x values
x_vals = np.linspace(-10, 10, 400)

# Convert the sympy function to a lambda function for plotting
f_lambdified = sp.lambdify(x, f, modules=[{"Heaviside": np.heaviside, "DiracDelta": sp.DiracDelta}, "numpy"])

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x_vals, f_lambdified(x_vals), label=str(f))

plt.legend()
plt.grid(True)
plt.show()
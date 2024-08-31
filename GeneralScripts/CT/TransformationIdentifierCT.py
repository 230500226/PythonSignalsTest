import numpy as np
from scipy import interpolate

# THIS IS INACCUARTE 

# Ask the user to input the time points and values for the function x(t)
x_t_values = input("Enter the time points for the function x(t), separated by commas: ").split(',')
x_values = input("Enter the values for the function x(t) at these time points, separated by commas: ").split(',')

# Ask the user to input the time points and values for the function y(t)
y_t_values = input("Enter the time points for the function y(t), separated by commas: ").split(',')
y_values = input("Enter the values for the function y(t) at these time points, separated by commas: ").split(',')

# Convert the inputs to numpy arrays
x_t = np.array([float(value) for value in x_t_values])
x = np.array([float(value) for value in x_values])
y_t = np.array([float(value) for value in y_t_values])
y = np.array([float(value) for value in y_values])

# Fit a polynomial function to the points
poly_func_x = np.poly1d(np.polyfit(x_t, x, deg=3))
poly_func_y = np.poly1d(np.polyfit(y_t, y, deg=3))

# Print the polynomial functions
print("x(t) = ", poly_func_x)
print("y(t) = ", poly_func_y)

# Estimate the transformations
A = poly_func_y.coeffs[0] / poly_func_x.coeffs[0]  # amplitude scaling factor
B = poly_func_y.coeffs[-1] - A * poly_func_x.coeffs[-1]  # amplitude shifting amount
C = y_t[1] / x_t[1]  # time scaling factor
D = y_t[0] - C * x_t[0]  # time shifting units

# Print the estimated transformations
print(f"Amplitude scaling by a factor of {A}.")
print(f"Amplitude shifting by {B} units.")
print(f"Time scaling by a factor of {C}.")
print(f"Time shifting by {D} units.")

# Construct the equation of y(t) in terms of x(t)
print(f"y(t) = {A} * x({C} * (t - {D})) + {B}")
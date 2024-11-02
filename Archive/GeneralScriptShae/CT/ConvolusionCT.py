import numpy as np
import scipy.interpolate as interpolate
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Get h(t) from user
h_indices = input("Enter indices for h(t): ").split(',')
h_values = input("Enter index values for h(t): ").split(',')
h_indices = np.array([float(index) for index in h_indices])
h_values = np.array([float(value) for value in h_values])
h = interpolate.interp1d(h_indices, h_values, fill_value="extrapolate")

# Get x(t) from user
x_indices = input("Enter indices for x(t): ").split(',')
x_values = input("Enter index values for x(t): ").split(',')
x_indices = np.array([float(index) for index in x_indices])
x_values = np.array([float(value) for value in x_values])
x = interpolate.interp1d(x_indices, x_values, fill_value="extrapolate")

t_vals = np.linspace(min(min(h_indices), min(x_indices)), max(max(h_indices), max(x_indices)), 1000)

def convolution(t):
    integrand = lambda tau: h(tau) * x(t - tau)
    lower_limit = max(min(h_indices), min(x_indices))
    upper_limit = min(max(h_indices), max(x_indices))
    result, _ = integrate.quad(integrand, lower_limit, upper_limit, limit=100, epsabs=1.49e-08, epsrel=1.49e-08)
    return result

h_vals = h(t_vals)
x_vals = x(t_vals)
y_vals = np.array([convolution(t) for t in t_vals])

plt.figure(figsize=(10, 6))

# Plot h(t)
plt.subplot(3, 1, 1)
plt.plot(t_vals, h_vals, label='h(t)')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.legend()
plt.grid(True)

# Plot x(t)
plt.subplot(3, 1, 2)
plt.plot(t_vals, x_vals, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)

# Plot convolution
plt.subplot(3, 1, 3)
plt.plot(t_vals, y_vals, label='Convolution of h(t) and x(t)')
plt.xlabel('t')
plt.ylabel('Convolution')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Ask the user for a value to check
t_check = float(input("Enter the y(t) to check: "))

# Calculate the convolution at that point
y_check = convolution(t_check)

# Print the result
print(f"Value at y({t_check}): {y_check}")
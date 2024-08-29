import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
t_vals = np.linspace(0, 5, 1000)

def h(t):
    return np.where(t >= 0, t, 0)  # h(t) = t * u(t)

def x(t):
    return np.where((t >= 1) & (t < 3), 1, 0)  # x(t) = u(t - 1) - u(t - 3)

def convolution(t):
    integrand = lambda tau: h(tau) * x(t - tau)
    result, _ = integrate.quad(integrand, -np.inf, np.inf)
    return result

y_vals = np.array([convolution(t) for t in t_vals])

plt.figure(figsize=(10, 6))
plt.plot(t_vals, y_vals, label='Convolution of h(t) and x(t)')
plt.xlabel('t')
plt.ylabel('Convolution')
plt.title('Continuous Convolution of h(t) and x(t)')
plt.legend()
plt.grid(True)
plt.show()

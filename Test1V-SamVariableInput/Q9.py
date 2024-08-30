import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def get_function_from_user(prompt, example):
    print(f"Example: {example}")
    func_str = input(prompt)
    def func(t):
        u = lambda t: np.where(t >= 0, 1, 0)
        return eval(func_str)
    return func

h = get_function_from_user("Enter the h(t) function in the format 't * u(t)': ", "h(t) = t * u(t)")
x = get_function_from_user("Enter the x(t) function in the format 'u(t - 1) - u(t - 3)': ", "x(t) = u(t - 1) - u(t - 3)")

t_vals = np.linspace(0, 5, 1000)

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
from scipy.integrate import quad
import sympy as sm

t = sm.Symbol('t')
u = sm.Heaviside
x = (t+6)*(u(t+6)-u(t+3)) + 3*(u(t+3)- u(t+1)) + (-t+2)*(u(t+1)- u(t)) + 2*(u(t) - u(t-4)) 
# sm.plot(x, (t,-10,10)) # This is to confirm if the plot is correct, resembles the original function 
# even = (1/2)*(x(t)+x(-t))
even = (x+x.subs(t, -t))/2
data = sm.lambdify(t, even, 'numpy')
result, error = quad(data, -3, 3)
print(result)
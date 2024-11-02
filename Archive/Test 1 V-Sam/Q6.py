import sympy as sm
from scipy.integrate import quad
t = sm.Symbol('t')
u = sm.Heaviside
x = 5*u(t+4)+2*u(t+1)-3*u(t-3)-4*u(t-5)
sm.plot(x, (t, -10, 10)) # Just to confirm if the graph really looks the same as it is supposed to 
data = sm.lambdify(t, x, 'numpy')
result, error = quad(data, -2, 3)
print("Results: ",result)
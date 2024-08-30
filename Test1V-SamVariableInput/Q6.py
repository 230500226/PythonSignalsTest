import sympy as sm
from scipy.integrate import quad

t = sm.Symbol('t')
u = sm.Heaviside

print("Enter your function. For example: 5*u(t+4)+2*u(t+1)-3*u(t-3)-4*u(t-5)")
# this graph is correct check it out in desmos f(t)=5H(t+4)+2H(t+1)-3H(t-3)-4H(t-5)
user_input = input("Enter your function: ")
x = sm.sympify(user_input, {"u": u})

sm.plot(x, (t, -10, 10)) 

data = sm.lambdify(t, x, 'numpy')
result, error = quad(data, -2, 3)
print("Results: ",result)
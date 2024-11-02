import sympy as sm
from scipy.integrate import quad 
t = sm.Symbol('t')
u = sm.Heaviside

# User input the function x
import sympy as sm

def get_piecewise_function():
    t = sm.Symbol('t')
    pieces = []
import sympy as sm
from scipy.integrate import quad 
t = sm.Symbol('t')
u = sm.Heaviside
x = (t+6)*(u(t+6)-u(t+3)) + 3*(u(t+3)- u(t+1)) + (-t+2)*(u(t+1)- u(t)) + 2*(u(t) - u(t-2)) + (-t+4)*(u(t-2) - u(t-4))
y = 2*x.subs(t, (3-t)) # Does the time shifting transformarion
data = sm.lambdify(t, y, 'numpy') # Changes the format function from sympy to an array that is understood by the scipy library to better deal with intergrals
result, error = quad(data, 1, 5) # This function returns results and the error of the output
print("Integral of y(t) from t=1 to t=5:",result)
# p1 = sm.plot(x, (t, -10, 10), show=False, line_color='blue', label='x(t)')
# p2 = sm.plot(y, (t, -10, 10), show=False, line_color='red', label='y(t)')
# p1.extend(p2)
# p1.show()
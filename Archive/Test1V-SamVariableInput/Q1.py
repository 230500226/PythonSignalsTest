import sympy as sm
from scipy.integrate import quad 
t = sm.Symbol('t')
u = sm.Heaviside

def get_piecewise_function():
    t = sm.Symbol('t')
    pieces = []
    print("Example of a function to input: start value 0, end value 3 for interval -6 to -3, start value 3, end value 3 for interval -3 to -1, start value 2, end value 0 for interval -1 to 0, start value 2, end value 2 for interval 0 to 2, start value 4, end value 0 for interval 2 to 4")
    while True:
        start = input("Enter the start of the interval (or 'done' to finish): ")
        if start == 'done':
            break
        end = input("Enter the end of the interval: ")
        start_value = input("Enter the function value at the start of the interval: ")
        end_value = input("Enter the function value at the end of the interval: ")
        condition = sm.And(t >= float(start), t < float(end))
        function = sm.sympify(start_value) + (sm.sympify(end_value) - sm.sympify(start_value)) * (t - float(start)) / (float(end) - float(start))
        pieces.append((function, condition))
    return sm.Piecewise(*pieces)

x = get_piecewise_function()
sm.pprint(x)
x = (t+6)*(u(t+6)-u(t+3)) + 3*(u(t+3)- u(t+1)) + (-t+2)*(u(t+1)- u(t)) + 2*(u(t) - u(t-2)) + (-t+4)*(u(t-2) - u(t-4))
y = 2*x.subs(t, (3-t)) # Does the time shifting transformarion
data = sm.lambdify(t, y, 'numpy') # Changes the format function from sympy to an array that is understood by the scipy library to better deal with intergrals
result, error = quad(data, 1, 5) # This function returns results and the error of the output
print("Integral of y(t) from t=1 to t=5:",result)
# p1 = sm.plot(x, (t, -10, 10), show=False, line_color='blue', label='x(t)')
# p2 = sm.plot(y, (t, -10, 10), show=False, line_color='red', label='y(t)')
# p1.extend(p2)
# p1.show()
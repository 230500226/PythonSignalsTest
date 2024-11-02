import sympy as sm
from scipy.integrate import quad 

# Note: not sure if this is correct?

def get_piecewise_function():
    t = sm.Symbol('t')
    pieces = []
    print("Example of a function to input: start value 0, end value 3 for interval -6 to -3, start value 3, end value 3 for interval -3 to -1, start value 3, end value 2 for interval -1 to 0, start value 2, end value 2 for interval 0 to 2, start value 2, end value 0 for interval 2 to 4")
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

t = sm.Symbol('t')
x = get_piecewise_function()
sm.pprint(x)

even = (x+x.subs(t, -t))/2
data = sm.lambdify(t, even, 'numpy')

lower_bound = float(input("Enter the lower bound of the integral: "))
upper_bound = float(input("Enter the upper bound of the integral: "))

result, error = quad(data, lower_bound, upper_bound)
print(result)
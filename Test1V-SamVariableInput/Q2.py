import sympy as sm

def heaviside_function(t):
    u = sm.Heaviside
    return u(t)

def calculate_y(x, y_prev, a):
    return x + a * y_prev

def parse_input(input_string):
    # Remove 'u(t)' from the input and convert the rest to a float
    return float(input_string.replace('u(t)', ''))

def calculate_sequence(a, n, x_coefficient):
    t = sm.Symbol('t')
    x = x_coefficient * heaviside_function(t)
    y_prev = 0
    for i in range(n):
        y = calculate_y(x, y_prev, a)
        y_prev = y
    # Replace Heaviside(t) with 1 to get a numerical output
    y = y.subs(sm.Heaviside(t), 1)
    return y

# Get user input for x(n)
x_input = input("Enter the value for x(n) like tihs '2u(t)': ")
x_coefficient = parse_input(x_input)

# Get user input for a
a = float(input("Enter the value for a: "))

# Calculate the sequence for 3 steps
n = 3
y = calculate_sequence(a, n, x_coefficient)
print(y)
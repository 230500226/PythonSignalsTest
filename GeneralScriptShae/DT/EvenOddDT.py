
import sympy as sm
from scipy.integrate import quad
import numpy as np

# Define the actual symbol/ Variable
t = sm.Symbol('t')

# Define the Original Function
def input_piecewise():
    # Ask the user for the number of pieces
    num_pieces = int(input("Enter the number of pieces: "))

    # Initialize the pieces list
    pieces = []

    # For each piece
    for i in range(num_pieces):
        # Ask the user for the condition and function
        condition = input(f"Enter the condition for piece {i+1} (e.g., '(t > -6) & (t < -3)'): ")
        func = input(f"Enter the function for piece {i+1} (e.g., 't + 6'): ")

        # Append the piece to the pieces list
        pieces.append((sm.sympify(func), sm.sympify(condition)))

    # Add the default piece (0, True)
    pieces.append((0, True))

    # Create the Piecewise function
    t = sm.Symbol('t')
    equation = sm.Piecewise(*pieces)

    return equation

# Test the function
equation = input_piecewise()
print("The piecewise function is:", equation)

# Define the Flipped Function
flipped_equation = equation.subs(t, -t)

# Finding the Even Component
xeven = (equation + flipped_equation) / 2
xodd = (equation-flipped_equation) / 2
xeven_func = sm.lambdify(t, xeven, 'numpy') # Convert the even component to a lambda function for integration
xodd_func = sm.lambdify(t, xodd, 'numpy')
inter, miss = quad(xodd_func, -3, 3)
result, error = quad(xeven_func, -3, 3)
print("Integration even result:", result)
print("Integration odd result:", inter)
# print("Integration error:", error)
# sm.plot(equation, flipped_equation, (t, -8, 8), show=True, legend=True, labels=['Original Function', 'Flipped Function'])

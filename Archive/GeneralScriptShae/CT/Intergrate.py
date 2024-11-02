# import sympy as sp
# # Define symbolic variables
# t = sp.Symbol('t')
# tau = sp.Symbol('tau')
# x = sp.sin(t)
# # Perform intergration
# inter = sp.integrate(x, (t, 0, t)) #t is the main variable, intergrating from 0 to t
# # Display the result
# sp.pprint(inter)

import sympy as sp  # Import the sympy library for symbolic computation

# Define symbolic variables
t = sp.Symbol('t')  # Define a symbolic variable t
tau = sp.Symbol('tau')  # Define another symbolic variable tau

# Define a function with Heaviside and delta functions
x = sp.Heaviside(t - tau) * sp.DiracDelta(t - 2*tau)  # Define a function x which is the product of a Heaviside function and a Dirac delta function

# Perform integration
# The integrate function takes three arguments: the function to integrate, the variable to integrate with respect to, and the lower and upper bounds of integration.
# Here, we are integrating the function x with respect to t from -infinity to +infinity.
# The lower and upper bounds of integration can be any real numbers or -sp.oo/+sp.oo for -infinity/+infinity.
# Changing these bounds will change the result of the integration.
inter = sp.integrate(x, (t, -sp.oo, sp.oo)) 

# Display the result
# pprint stands for "pretty print". It prints the result in a more readable format.
sp.pprint(inter)
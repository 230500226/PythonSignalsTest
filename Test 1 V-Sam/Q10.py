import sympy as sm

t = sm.Symbol('t')
x = sm.Piecewise(((t+20)/2, (t > -20) & (t < 0)), ((-t+10), (t > 0) & (t < 10)), (0, True))
#  Output is = x(3)
print("The results are : x(3): ",x.subs(t, 3))
# sm.plot(x, (t, -30, 15,))
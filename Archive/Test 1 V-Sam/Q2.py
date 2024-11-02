# Time delaying that depends on the previous output,
# y[n] = x[n] + a*y[n-1] => a = 0.7
import sympy as sm
t = sm.Symbol('t')
u = sm.Heaviside
x = u(t)
y0 = 0
for i in range(3):
    print(i)
    y = 2 + 0.7 * y0
    y0 = y
print(y)
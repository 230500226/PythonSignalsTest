# Time delaying that depends on the previous output,
# y[n] = x[n] + a*y[n-1] where a = 0.4 and x[n] = u(t)
# y[n] = u(t) + 0.4*y[n-1]
import sympy as sm
t = sm.Symbol('t')
u = sm.Heaviside
x = 3*u(t)
y0 = 0
for i in range(5): #y[4]
    y = x + 0.4 * y0
    y0 = y
    print(str(i) +"\t"+ str(y))
print(y)

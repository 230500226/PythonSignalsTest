import sympy as sp 
t = sp.Symbol('t')
equation = sp.sin(t)
T = 10  
forier = sp.fourier_series(equation, (t, 0, T))
truncated_series = forier.truncate(40)
sp.pprint(truncated_series.rewrite(sp.exp))
p1 = sp.plot(truncated_series, (t, 0, T), show=False, line_color='blue', label='Fourier Series')
p2 = sp.plot(equation, (t, 0, T), show=False, line_color='red', label='Original Function')
p1.extend(p2)
p1.show()

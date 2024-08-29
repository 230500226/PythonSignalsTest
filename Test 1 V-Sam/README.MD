# Observations 
<table> 
<tr>
<th> Functinality </th>
<th> Continious Signals </th>
<th> Discrete Signals </th>
</tr>
<tr>
<td> Convolution </td>
<td> When Dealing with Continous functions, `scipy.intergrate` gives reliable results. see `Q9.py`</td>
<td> `numpy.convolve` has proven to give reliable results, see `Q11.py`</td>
</tr>
<tr>
<td> Plotting </td>
<td> It is very important to always try to see that the original functions are corrsponding to what they are supposed to be. With `sympy` you can do this in less than 10 lines, so, it is preffered for continous signals, `matplotlib.pyplot` could be used too, it also gives accurate results. See `Q6.py` and `Q9.py` </td>
<td> I haven't tried using `sympy` for plotting discrete functions, but `matplotlib.pyplot` has been working wonders, so i am sticking with that for now. See `Q7.py` </td>
</tr>
<tr>
<td> Time Shifting </td>
<td> `sympy` handles this much easier using `equation.subs(variable or symbol, the transformation)`, this has been implemented on `Q1.py` </td>
<td> `numpy` is always good with discrete functions, to shift data, we use `np.roll(array, how many units)`. See `Q7.py` </td>
</tr>
<tr>
<td> Intergration </td>
<td> `sympy` is a great tool for symbolic calculations, but it turns out to not give accurate results.. For this we use both `sympy` and `scipy.integrate`. See `Q1.py` and `Q4.py` </td>
<td> Integral is not applicable for discrete functions, instead we use summation. with this i have used `numpy`, and its functionalities to shift data around and select the data from specific indices to to sum them using `np.sum(selected_data)`. See `Q7.py` </td>
</tr>
</table

# Observations 

<table> 
<tr>
<th> Functionality </th>
<th> Continuous Signals </th>
<th> Discrete Signals </th>
</tr>
<tr>
<td> Convolution </td>
<td> When dealing with continuous functions, `scipy.integrate` provides reliable results for convolution. See `q9.py` for an example. </td>
<td> For discrete signals, `numpy.convolve` is highly effective and has proven to give reliable results. See `q11.py` for an example. </td>
</tr>
<tr>
<td> Plotting </td>
<td> For continuous signals, `sympy.plot` can be used to quickly verify if the functions correspond to their expected behavior. However, `matplotlib.pyplot` is also suitable and provides accurate visualizations. See `q6.py` and `q9.py`. </td>
<td> `SymPy` does not natively support plotting discrete functions well, so `matplotlib.pyplot` is preferred for this purpose. It provides clear and accurate plots for discrete data. See `q7.py`. </td>
</tr>
<tr>
<td> Time Shifting </td>
<td> `SymPy` makes time shifting easy with `equation.subs(variable, transformation)`, allowing for straightforward symbolic manipulation. See `q1.py`. </td>
<td> For discrete functions, `numpy` handles time shifting efficiently using `np.roll(array, shift_amount)`, which is effective for manipulating discrete data. See `q7.py`. </td>
</tr>
<tr>
<td> Integration </td>
<td> `SymPy` is great for symbolic integration but may not always provide numerical accuracy. For numerical integration, `scipy.integrate` is preferred. Combining both tools can be effective. See `q1.py` and `qq4.py`. </td>
<td> Integration is not typically applicable to discrete signals. Instead, summation is used, which can be handled efficiently with `numpy`. Data selection and summation are demonstrated using `np.sum(selected_data)`. See `q7.py`. </td>
</tr>
</table>

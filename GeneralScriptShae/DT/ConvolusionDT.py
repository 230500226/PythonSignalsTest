import sympy as sp

# Step 1: Define the symbol
x = sp.symbols('x')

# Step 2: Prompt the user to input the range of values for x
fx_min = int(input("Enter the minimum value of x: "))
fx_max = int(input("Enter the maximum value of x: "))
n = int(input("Enter the n value: "))

hx_min = int(input("Enter the minimum value of x: ")) + n
hx_max = int(input("Enter the maximum value of x: ")) + n

min = fx_min if fx_min < hx_min else hx_min
max = fx_max if fx_max > hx_max else hx_max

# Step 3: Initialize empty dictionaries to store function values for f and h
f_values = {}
h_values = {}

# Step 4: Prompt the user to input the function value for each x in the range for f(x)
print("Enter the values for the function f(x):")
for i in range(fx_min, fx_max + 1):
    value = int(input(f"f({i}) = "))
    f_values[i] = value

# Step 5: Prompt the user to input the function value for each x in the range for h(x)
print("Enter the values for the function h(x):")
for i in range(hx_min - n, hx_max + 1 - n):
    value = int(input(f"h({i}) = "))
    h_values[i] = value

# Step 6: Display the function values and their range
print("The function values for f(x) are:")
for key, value in f_values.items():
    print(f"f({key}) = {value}")

print("The function values for h(x) are:")
for key, value in h_values.items():
    print(f"h({key}) = {value}")

print(f"The range of fx is: [{fx_min}, {fx_max}]")

# Step 7: Calculate the sum of f(k-1) * h(k)
sum_result = 0
h = list(h_values.values())
h = h[::-1]

def shiftH(h):
    if (n < 0):
        h = [0] * (abs(n)) + h
        h = [0] * (max - min - len(h)-1) + h
    else:
        h = [0] * abs(n) +  h
        h = h + [0] * (max - min -len(h)-1)
    return h

h = shiftH(h)

f = list(f_values.values())
print((f))
print((h))

for k in range(len(f)):
    sum_result += f[k] * h[k]

# Step 8: Display the sum
print(f"The sum of f(k-1) * h(k) from k={min + 1} to k={max} is: {sum_result}")

import sympy as sp

# Step 1: Define the symbol
x = sp.symbols('x')

# Step 2: Prompt the user to input the range of values for x
fx_min = int(input("Enter the minimum value of x: "))
fx_max = int(input("Enter the maximum value of x: "))
n = int(input("Enter the n value: "))

hx_min = int(input("Enter the minimum value of x: ")) + n
hx_max = int(input("Enter the maximum value of x: ")) + n

min_val = min(fx_min, hx_min - n)
max_val = max(fx_max, hx_max - n)

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

# Step 7: Calculate the sum of f(k) * h(k)
length = max_val - min_val + 1

def shiftH(h, n, length):
    if n > 0:
        h = [0] * n + h
    else:
        h = h + [0] * abs(n)
    return h[:length]

# Prepare f and h arrays
f = [f_values.get(i, 0) for i in range(min_val, max_val + 1)]
h = [h_values.get(i, 0) for i in range(min_val, max_val + 1)]
h = shiftH(h[::-1], n, length)  # Fixing the direction of shift

print("Array f:", f)
print("Array h:", h)

# Ensure both arrays are of equal length
if len(f) != len(h):
    max_len = max(len(f), len(h))
    f.extend([0] * (max_len - len(f)))
    h.extend([0] * (max_len - len(h)))

sum_result = sum(f[k] * h[k] for k in range(len(f)))

# Step 8: Display the sum
print(f"The sum of f(k) * h(k) from k={min_val} to k={max_val} is: {sum_result}")

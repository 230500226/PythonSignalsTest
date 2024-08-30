import sympy as sp

# Step 1: Define the symbol
x = sp.symbols('x')

# Step 2: Prompt the user to input the range of values for x
x_min = int(input("Enter the minimum value of x: "))
x_max = int(input("Enter the maximum value of x: "))

# Step 3: Initialize empty dictionaries to store function values for f and h
f_values = {}
h_values = {}

# Step 4: Prompt the user to input the function value for each x in the range for f(x)
print("Enter the values for the function f(x):")
for i in range(x_min, x_max + 1):
    value = float(input(f"f({i}) = "))
    f_values[i] = value

# Step 5: Prompt the user to input the function value for each x in the range for h(x)
print("Enter the values for the function h(x):")
for i in range(x_min, x_max + 1):
    value = float(input(f"h({i}) = "))
    h_values[i] = value

# Step 6: Display the function values and their range
print("The function values for f(x) are:")
for key, value in f_values.items():
    print(f"f({key}) = {value}")

print("The function values for h(x) are:")
for key, value in h_values.items():
    print(f"h({key}) = {value}")

print(f"The range of x is: [{x_min}, {x_max}]")

# Step 7: Calculate the sum of f(k-1) * h(k)
sum_result = 0
for k in range(x_min + 1, x_max + 1):
    sum_result += f_values[k - 1] * h_values[k]

# Step 8: Display the sum
print(f"The sum of f(k-1) * h(k) from k={x_min + 1} to k={x_max} is: {sum_result}")
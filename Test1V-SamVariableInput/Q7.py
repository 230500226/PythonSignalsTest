import numpy as np

# Fixed index range from -10 to 9
n = np.arange(-10, 10)

# Ask the user to input the values for each index
x = []
for i in n:
    value = float(input(f"Enter the value for index {i}: "))
    x.append(value)

# Calculate y
y = 0.5*(np.roll(x, 3)+x)

# Find the indices where n is between -3 and 3
indices = np.where((n >= -3) & (n <= 3))

# Print the sum of the results
print("The sum of the results is : ",np.sum(y[indices]))
import numpy as np

# Ask the user for the start and end indices for x and h
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

# Generate the n array using the start and end indices
n = np.arange(start_index, end_index + 1)

# Ask the user to input the values for x at each index
x = []
for i in range(start_index, end_index + 1):
    x_value = int(input(f"Enter the value for x at index {i}: "))
    x.append(x_value)

# Ask the user to input the values for h at each index
h = []
for i in range(start_index, end_index + 1):
    h_value = int(input(f"Enter the value for h at index {i}: "))
    h.append(h_value)

# Perform the convolution operation
y = np.convolve(x, h, mode = "same")

# Find the index where n equals 1
Index = np.where(n == 1)

# Print the convolution at that index
print(f"The convolution at y[{Index}] = {y[Index]}")
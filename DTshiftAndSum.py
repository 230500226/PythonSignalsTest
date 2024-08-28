# Define the discrete function with user input
def get_user_defined_discrete_function():
    values = {}
    start_index = int(input("Enter the start index of the discrete function: "))
    end_index = int(input("Enter the end index of the discrete function: "))
    
    for i in range(start_index, end_index + 1):
        value = int(input(f"Enter the value for index {i}: "))
        values[i] = value
    
    return values

# Get user-defined values
user_defined_values = get_user_defined_discrete_function()

def discrete_function(x):
    return user_defined_values.get(x, 0)  # Return 0 if x is not in the dictionary

# Create the array
x_values = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y_values = [discrete_function(x) for x in x_values]

# Define the shifted function
def shifted_function(x):
    return discrete_function(x + 3)

# Create the array for the shifted function
shifted_y_values = [shifted_function(x) for x in x_values]

# Define the sum function
def sum_function(x):
    return discrete_function(x) + shifted_function(x)

# Define the multipl function
def multipl_function(x):
    return sum_function(x) * 0.5

# Create the array for the sum function
sum_y_values = [sum_function(x) for x in x_values]

# Create the array for the multipl function
multipl_y_values = [multipl_function(x) for x in x_values]

# Add the values from the multipl function for x indices -2 to 2
indices_to_sum = range(-2, 3)
sum_multipl_values = sum(multipl_function(x) for x in indices_to_sum)

# Print the result
print("Sum of multipl function values from x = -2 to x = 2:", sum_multipl_values)
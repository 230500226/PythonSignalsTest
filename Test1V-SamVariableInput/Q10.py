import sympy as sm

t = sm.Symbol('t')

# Print instructions
print("Enter the indexes and values one by one. Press 'q' when done.")

# Get user input
points = []
while True:
    index = input("Enter the index: ")
    if index.lower() == 'q':
        break
    value = input("Enter the value for index {}: ".format(index))
    points.append((int(index), int(value)))

# Sort points by index
points.sort(key=lambda x: x[0])

# Create piecewise function
conditions = []
for i in range(len(points) - 1):
    slope = (points[i+1][1] - points[i][1]) / (points[i+1][0] - points[i][0])
    conditions.append((points[i][1] + slope * (t - points[i][0]), (t >= points[i][0]) & (t < points[i+1][0])))

# Add a default condition for all other cases
conditions.append((0, True))

x = sm.Piecewise(*conditions)

# Output
print("The results are : x(3): ",x.subs(t, 3))
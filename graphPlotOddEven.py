import matplotlib.pyplot as plt
import numpy as np

def get_intervals():
    intervals = []
    while True:
        try:
            start_index = input("Enter the start index (interval {0}): ".format(len(intervals) + 1))
            if start_index.lower() == 'q':
                break
            start_index = float(start_index)
            
            start_value = float(input("Enter the start value (interval {0}): ".format(len(intervals) + 1)))
            end_index = float(input("Enter the end index (interval {0}): ".format(len(intervals) + 1)))
            end_value = float(input("Enter the end value (interval {0}): ".format(len(intervals) + 1)))
            
            intervals.append((start_index, start_value, end_index, end_value))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
    return intervals

def generate_points(intervals):
    points = []
    for start_index, start_value, end_index, end_value in intervals:
        slope = (end_value - start_value) / (end_index - start_index)
        for i in range(int(start_index), int(end_index) + 1):
            value = start_value + slope * (i - start_index)
            points.append((i, value))
    return points

def plot_intervals(points, title):
    plt.figure()
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.plot(x_values, y_values, marker='o')
    
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(np.floor(min(x_values)), np.ceil(max(x_values)) + 1, 1))
    plt.yticks(np.arange(np.floor(min(y_values)), np.ceil(max(y_values)) + 1, 1))
    
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)

def calculate_even_odd(points):
    x_values = {point[0]: point[1] for point in points}
    
    min_index = int(min(x_values.keys()))
    max_index = int(max(x_values.keys()))
    
    even_points = []
    odd_points = []
    
    for n in range(min_index, max_index + 1):
        x_n = x_values.get(n, 0)
        x_neg_n = x_values.get(-n, 0)
        
        Xe_n = 0.5 * (x_n + x_neg_n)
        Xo_n = 0.5 * (x_n - x_neg_n)
        
        even_points.append((n, Xe_n))
        odd_points.append((n, Xo_n))
    
    return even_points, odd_points

def plot_even_odd(even_points, odd_points):
    plt.figure()
    
    x_even = [point[0] for point in even_points]
    y_even = [point[1] for point in even_points]
    plt.plot(x_even, y_even, label='Even Component', marker='o')
    
    x_odd = [point[0] for point in odd_points]
    y_odd = [point[1] for point in odd_points]
    plt.plot(x_odd, y_odd, label='Odd Component', marker='x')
    
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(np.floor(min(x_even + x_odd)), np.ceil(max(x_even + x_odd)) + 1, 1))
    plt.yticks(np.arange(np.floor(min(y_even + y_odd)), np.ceil(max(y_even + y_odd)) + 1, 1))
    
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Even and Odd Components')
    plt.legend()

def main():
    print("Enter function intervals. Type 'q' to stop.")
    intervals = get_intervals()
    
    if intervals:
        points = generate_points(intervals)
        plot_intervals(points, "Original Graph")
        
        even_points, odd_points = calculate_even_odd(points)
        plot_even_odd(even_points, odd_points)
        
        plt.show()
    else:
        print("No intervals entered. Exiting.")

if __name__ == "__main__":
    main()

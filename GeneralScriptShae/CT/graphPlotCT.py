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

def plot_intervals(intervals, title):
    plt.figure()
    for interval in intervals:
        start_index, start_value, end_index, end_value = interval
        plt.plot([start_index, end_index], [start_value, end_value], marker='o')
    
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(np.floor(min(interval[0] for interval in intervals)), np.ceil(max(interval[2] for interval in intervals)) + 1, 1))
    plt.yticks(np.arange(np.floor(min(interval[1] for interval in intervals)), np.ceil(max(interval[3] for interval in intervals)) + 1, 1))
    
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)

def transform_intervals(intervals, x_shift, y_shift, time_scale, amp_scale, time_reverse, amp_reverse):
    transformed_intervals = []
    for interval in intervals:
        start_index, start_value, end_index, end_value = interval
        start_index, end_index = start_index * time_scale, end_index * time_scale
        start_value, end_value = start_value * amp_scale, end_value * amp_scale
        if time_reverse:
            start_index, end_index = -end_index, -start_index
            start_value, end_value = end_value, start_value  # Reverse values accordingly
        if amp_reverse:
            start_value, end_value = -start_value, -end_value
        transformed_intervals.append((start_index + x_shift, start_value + y_shift, end_index + x_shift, end_value + y_shift))
    return transformed_intervals

def main():
    print("Enter function intervals. Type 'q' to stop.")
    intervals = get_intervals()
    
    if intervals:
        try:
            x_shift = float(input("Enter the x shift value: "))
            y_shift = float(input("Enter the y shift value: "))
            time_scale = float(input("Enter the time scale value (positive): "))
            amp_scale = float(input("Enter the amplitude scale value (positive): "))
            if time_scale <= 0 or amp_scale <= 0:
                raise ValueError("Scale values must be positive.")
            time_reverse = input("Do you want to apply time reversal? (y/n): ").lower() == 'y'
            amp_reverse = input("Do you want to apply amplitude reversal? (y/n): ").lower() == 'y'
            
            plot_intervals(intervals, "Original Graph")
            transformed_intervals = transform_intervals(intervals, x_shift, y_shift, time_scale, amp_scale, time_reverse, amp_reverse)
            plot_intervals(transformed_intervals, "Transformed Graph")
            
            plt.show()
        except ValueError as e:
            print(f"Invalid input: {e}")
    else:
        print("No intervals entered. Exiting.")

if __name__ == "__main__":
    main()

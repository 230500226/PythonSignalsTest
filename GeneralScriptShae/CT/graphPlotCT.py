import matplotlib.pyplot as plt

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

def plot_intervals(intervals):
    for interval in intervals:
        start_index, start_value, end_index, end_value = interval
        plt.plot([start_index, end_index], [start_value, end_value], marker='o')
    
    # Adding grid lines for each unit
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Adding ticks for each unit
    plt.xticks(range(int(min(interval[0] for interval in intervals)), int(max(interval[2] for interval in intervals)) + 1))
    plt.yticks(range(int(min(interval[1] for interval in intervals)), int(max(interval[3] for interval in intervals)) + 1))
    
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Function Plot with Intervals')
    plt.show()

def main():
    print("Enter function intervals. Type 'q' to stop.")
    intervals = get_intervals()
    if intervals:
        plot_intervals(intervals)
    else:
        print("No intervals entered. Exiting.")

if __name__ == "__main__":
    main()

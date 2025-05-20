import numpy as np
from sum_calculator import multi_process_sum

def main():
    array = np.random.rand(1000000000)
    num_processes = 16  # You can change this to the number of CPU cores you want to use
    multi_process_sum(array, num_processes)

if __name__ == "__main__":
    main()
# cython: language_level=3
import numpy as np
from multiprocessing import Process
import multiprocessing

def sum_array(double[:] array):
    cdef double sum = 0
    cdef int i
    for i in range(len(array)):
        sum += array[i]
    return sum

def multi_process_sum(double[:] array, int num_processes):
    cdef int array_size = len(array)
    cdef int chunk_size = array_size // num_processes
    cdef int remainder = array_size % num_processes
    cdef int i

    processes = []
    cdef double[:] chunk

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else array_size
        chunk = array[start:end]
        process = Process(target=calculate_sum, args=(chunk,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

def calculate_sum(double[:] array):
    cdef double sum = 0
    cdef int i
    for i in range(len(array)):
        sum += array[i]

def main():
    array = np.random.rand(1000000)
    num_processes = multiprocessing.cpu_count()
    print(f"Number of processes: {num_processes}")
    multi_process_sum(array, num_processes)

if __name__ == "__main__":
    main()
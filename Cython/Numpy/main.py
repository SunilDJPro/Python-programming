# main.py
import numpy as np
import np_dot_prod  # Import the compiled Cython module

a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)

# Time the Cython version
import time
start_time = time.time()
result_cython = np_dot_prod.np_dot_prod(a, b)
end_time = time.time()
print(f"Cython time: {end_time - start_time:.4f} seconds")

# Time the NumPy version
start_time = time.time()
result_numpy = a @ b  # NumPy's dot product operator
end_time = time.time()
print(f"NumPy time: {end_time - start_time:.4f} seconds")

print(f"Result (Cython): {result_cython}")
print(f"Result (NumPy): {result_numpy}")
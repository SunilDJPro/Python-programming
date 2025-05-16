# cython: language_level=3
cimport numpy as np 

def np_dot_prod(np.ndarray[np.float64_t, ndim = 2] a, np.ndarray[np.float64_t, ndim = 2] b) -> double:

    cdef int i, j
    cdef double sum = 0
    cdef int rows_a = a.shape[0]
    cdef int cols_a = a.shape[1]
    cdef int cols_b = b.shape[1]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                sum += a[i, k] * b[k, j]

    return sum    
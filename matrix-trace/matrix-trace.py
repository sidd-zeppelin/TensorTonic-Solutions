import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    A = np.asarray(A, dtype=np.float64)
    tr = float(0.0)
    for i in range(len(A)):
        tr += A[i][i]

    return tr
    pass
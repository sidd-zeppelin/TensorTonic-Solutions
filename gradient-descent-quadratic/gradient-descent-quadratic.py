import numpy as np

def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    
    for n in range(steps):
        dL_dx = 2*a*x0 + b
        x0 = x0 - lr*dL_dx

    return x0
    pass
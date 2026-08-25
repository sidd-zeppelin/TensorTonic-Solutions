import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here

    x = np.asarray(x, dtype=np.float64)

    if x.ndim==1:
        m = np.max(x)
        return (np.exp(x - m) / np.sum(np.exp(x - m))) 

    if x.ndim > 1:
        m = np.max(x, axis=1, keepdims=True)
        return (np.exp(x - m) / np.sum(np.exp(x - m), axis=1, keepdims=True)) 
    
    
    pass
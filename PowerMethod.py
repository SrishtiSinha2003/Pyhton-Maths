import numpy as np

def power_method(A, x, tol=1e-6, max_iters=100):
    x = x / np.linalg.norm(x)  
    for _ in range(max_iters):
        x_new = np.dot(A, x)  
        lambda_max = np.max(np.abs(x_new))  
        x_new = x_new / np.linalg.norm(x_new)  
        if np.allclose(x, x_new, atol=tol):  
            break
        x = x_new  
    return x

A = np.array([[4, 1, 0], [0, 2, 1], [0, 0, 1]])
x0 = np.array([1, 1, 1])
dominant_eigenvector = power_method(A, x0)
print("Approximate Dominant Eigenvector: ")
print("\n".join([f"{val:6f}" for val in dominant_eigenvector]))
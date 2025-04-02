# Define a square matrix
A = np.array([[2, 1],
                [3, 3]])
x0 = np.array([1, 1])
eigenvalue, eigenvector = rayleigh_power_method(A, x0)
print("Dominant Eigenvalue:", eigenvalue)
print("Corresponding Eigenvector:", eigenvector)
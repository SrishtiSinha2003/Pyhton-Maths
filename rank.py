import copy
import numpy as np
A = [
    [1, 2, -1],
    [-2, 2, 3],
    [2, 0, 4]
]
B = [6, 3, 4]
AB = copy.deepcopy(A)
for i in range(0, len(A)):
    AB[i].append(B[i])
AB_np = np.array(AB)
print("A matrix : \n", A)
print("Augmented matrix (A : B) : \n", AB_np)
rank = np.linalg.matrix_rank(AB_np)
print("Rank of the augmented matrix is:", rank)
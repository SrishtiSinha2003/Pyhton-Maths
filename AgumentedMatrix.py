# Define matrix A and vector B as lists
A = [[1, 2, -1],
     [-2, 2, 3],
     [2, 0, 4]]

B = [[6],
     [3],
     [4]]

# Construct the augmented matrix AB manually
AB = [A[i] + B[i] for i in range(len(A))]

# Print the augmented matrix
print("Augmented matrix AB:")
for row in AB:
    print(row)

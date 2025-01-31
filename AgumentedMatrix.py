A = [[1, 2, -1],
     [-2, 2, 3],
     [2, 0, 4]]

B = [[6],
     [3],
     [4]]

AB = [A[i] + B[i] for i in range(len(A))]

print("Augmented matrix AB:")
for row in AB:
    print(row)

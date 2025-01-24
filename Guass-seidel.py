def gauss_seidel(a, b, x, max_iterations):
    n = len(a)
    for k in range(max_iterations):
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += a[i][j] * x[j]
            x[i] = (b[i] - sum) / a[i][i]
        print(f"Iteration {k+1}: {x}")
    return x
a = [[4, 1, 2], 
     [3, 5, 1], 
     [1, 1, 3]] 

b = [4, 7, 3] 

x = [0, 0, 0]  

max_iterations = 4  

solution = gauss_seidel(a, b, x, max_iterations)

print("Approximate solution:", solution)
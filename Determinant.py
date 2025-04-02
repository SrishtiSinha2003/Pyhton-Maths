import sympy as sp

A = [[22, 77, 11],
     [33, 23, 89],
     [55, 100, 100]]
A1 = sp.Matrix(A)      

det_A1 = A1.det() 
detA1 = sp.det(A1)     
print("Determinant of A:", det_A1)

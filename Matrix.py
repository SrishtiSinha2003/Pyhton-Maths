a1, b1, c1 = 1, 2, 3  
a2, b2, c2 = 2, 4, 6 
determinant = a1 * b2 - a2 * b1

if determinant == 0:
    if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1 :
        print("Infinite solution")
    else:
        print("The system has no unique solution.")
else:
    A_inv_a1 = b2/determinant
    A_inv_b1 = -b1/determinant
    A_inv_a2 = -a2/determinant
    A_inv_b2 = a1/determinant

    x = A_inv_a1 * c1 + A_inv_b1 * c2
    y = A_inv_a2 * c1 + A_inv_b2 * c2

    print("Solution is x = {x} and y = {y}")

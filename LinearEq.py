a1, b1, c1 = 1, 2, 3  
a2, b2, c2 = 2, 4, 6 
determinant = a1 * b2 - a2 * b1

if determinant == 0:
    if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1 :
        print("Infinite solution")
    else:
        print("The system has no unique solution.")
else:
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    print(f"The solution is x = {x}, y = {y}")  
        
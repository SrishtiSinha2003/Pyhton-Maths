import sympy as sp
x = sp.symbols('x')
y = x**3 - 3*x**2 + 4
first_derivative = sp.diff(y, x)

# Find critical points (where the first derivative is zero)
critical_points = sp.solve(first_derivative, x)

# 
# Compute the second derivative
second_derivative = sp.diff(first_derivative, x)

# Determine maxima and minima using the second derivative test
for point in critical_points:
    second_derivative_value = second_derivative.subs(x, point)
    if second_derivative_value > 0:
        print(f"Local minimum at x = {point}")
    elif second_derivative_value < 0:
        print(f"Local maximum at x = {point}")
    else:
        print(f"Inconclusive at x = {point}")

print(f"Critical points: {critical_points}")

import sympy as sp
x = sp.symbols('x')
y = x**3 + 2*x**2 + x + 1
first_derivative = sp.diff(y, x)
second_derivative = sp.diff(first_derivative, x)
print(f"First derivative: {first_derivative}")
print(f"Second derivative: {second_derivative}")


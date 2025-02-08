def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = gcd_extended(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, x, y

def solve_linear_congruence(a, b, m):
    """Solve the linear congruence ax = b (mod m)."""
    g, x0, _ = gcd_extended(a, m)
    
    if b % g != 0:
        return None
    
    x0 = (x0 * (b // g)) % m
    solutions = [(x0 + i * (m // g)) % m for i in range(g)]
    return solutions

a, b, m = 14, 30, 100
print(solve_linear_congruence(a, b, m)) 
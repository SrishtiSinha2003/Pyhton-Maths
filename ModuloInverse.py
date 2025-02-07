def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        return gcd, y1, x1 - (a // b) * y1
    
    gcd, x, _ = extended_gcd(a, m)
    return x % m if gcd == 1 else None
a = 4
m = 5

print(f"GCD of {a} and {m} is: {gcd(a, m)}")

inverse = mod_inverse(a, m)
print(f"Modular inverse of {a} mod {m} is: {inverse}" if inverse else "Modular inverse does not exist.")

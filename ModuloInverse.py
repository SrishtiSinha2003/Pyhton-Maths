def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Modular inverse doesn't exist if gcd(a, m) != 1
    else:
        return x % m

# Example usage:
a = 4
m = 5

# Finding GCD
print(f"GCD of {a} and {m} is: {gcd(a, m)}")

# Finding modular inverse
inverse = mod_inverse(a, m)
if inverse:
    print(f"Modular inverse of {a} mod {m} is: {inverse}")
else:
    print("Modular inverse does not exist.")

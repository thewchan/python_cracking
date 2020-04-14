"""Contains two function of math manipulation for cryptanalysis."""


def gcd(a, b):
    """Return the greatest common divisor (GCD) of two positive integers using
     Euclid's algorithm.
    """
    while a != 0:
        a, b = (b % a), a

    return b


def find_mod_inverse(a, m):
    """Return the modular inverse of a % m, which is the number x such that
     a * x % m = 1.
    """
    if gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1 = u1 - (q * v1)
        v2 = u2 - (q * v2)
        v3 = u3 - (q * v3)
        u1, u2, u3 = v1, v2, v3

    return u1 % m

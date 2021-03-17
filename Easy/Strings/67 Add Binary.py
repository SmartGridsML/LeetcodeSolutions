# Given two binary strings a and b, return their sum as a binary string.
def addBinary(a: str, b: str) -> str:
    c = bin(int(a,2) + int(b,2))
    return str(c)[2:]

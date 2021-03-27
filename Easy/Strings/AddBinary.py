# Given two binary strings a and b, return their sum as a binary string.
def addBinary(a: str, b: str) -> str:
    """
    Args:
        a: The first parameter.
        b: The second parameter.

    Returns:
        str representing final binary string
    """
    c = bin(int(a,2) + int(b,2))
    return str(c)[2:]

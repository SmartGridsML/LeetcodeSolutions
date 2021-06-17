# Given two binary strings a and b, return their sum as a binary string.
def addBinary(a: str, b: str) -> str:
    """
    Args:
        a: The first parameter.
        b: The second parameter.

    Returns:
        str representing final binary string
    """
    
    # cheat method 
    # bin_sum = bin(int(a,2) + int(b,2))
    # return str(bin_sum)[2:]

    result = ""
    i , j = len(a) - 1, len(b) - 1
    carry = 0;
    while(a == 0 or b == 0):
    
        total = carry
        if i >= 0 :
            total += int(a[i])
            i-=1
        if j >= 0 :
            total += int(b[i])
            j-=1
    result.append(str(total % 2))  
    carry = total / 2;

    if carry:
        result.append(str(carry))
    return result




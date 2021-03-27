import re

def isPalindrome(s: str) -> bool:
    """
    Args:
        str: The second parameter.

    Returns:
        int representing max repeating string
    """
    my_copy = s.strip().lower()
    my_copy = "".join((char if char.isalpha() else "") for char in my_copy)
    #print(my_copy)
    #print("".join(reversed(my_copy)))
    return my_copy == "".join(reversed(my_copy))

print(isPalindrome("OP"))

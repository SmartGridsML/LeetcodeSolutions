# Given a string s, remove duplicate letters so that every letter appears once and only once.
#  You must make sure your result is the smallest in lexicographical order among all possible results.
import collections
import functools

def removeDuplicateLetters( s: str) -> str:
    result = "".join(collections.OrderedDict.fromkeys(s))
    std = functools.reduce(lambda x , y: x +y , sorted(result))
    return std

s = "cbacdcbc"
print(s)
s = removeDuplicateLetters(s)
print(s)

# Given a string s, sort it in decreasing
#  order based on the frequency of characters, and return the sorted string.
from collections import Counter

def frequencySort( s: str) -> str:
    counter = Counter(s)
    return ''.join(c * n for c, n in counter.most_common())

s = "tree"
t = frequencySort(s)
print(t)

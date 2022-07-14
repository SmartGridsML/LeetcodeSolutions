# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with those letters.

from collections import Counter

def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        for i in c.items():
            print(i)


s = 'abccccdd'
c = dict(Counter(s))
count = 0
print(c)
#for i  , j in c.items():
    
d = "ccc "
se = set(d)
print("se" , se)
print(d , len(set(d)))
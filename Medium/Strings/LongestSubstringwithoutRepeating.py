#  Given a string s, find the length of the longest substring without repeating characters.
# Hash table string two pinters sliding window
def lengthOfLongestSubstring(s: str) -> int:
    longSS = s[0]
    lengthSS = 1
    currSS = s[0]
    currLen = 1
    seen = {}
    for i , j in enumerate(s):
    #for i in range(1, len(s) + 1):
        curr = s[i]
        print(curr)
        while(j!=curr  ) :
            currSS+= j
            currLen +=1
        if len(longSS) < len(currSS):
            longSS = currSS
        if lengthSS < lengthSS:
            lengthSS = currLen
        #update current
        #curr = s[i + 1]
        print(curr)
    return lengthSS

a = "abcabc"
print(lengthOfLongestSubstring(a))

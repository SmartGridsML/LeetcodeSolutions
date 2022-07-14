"""
Return the minimum number of moves required so that all the characters of s are converted to 'O'.
"""
def minimumMoves(s:str) ->int:
    i = 0#
    res = 0
    n = len(s)
    while i < n:
        if s[i] == 'X':
            res+=1
            i+=3
        else:
            i+=1
        """
        #ALTERNATIVELY
        if s[i]=='O':
            i += 1
            continue
        else:
            ans += 1
            i += 3
        """
    return res

s = "XXOX"
o = minimumMoves(s) 
print(o) # expected 2
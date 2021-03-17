"""
Given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
Your task is to make these two strings equal to each other. You can swap any two characters 
that belong to different strings, which means: swap s1[i] and s2[j].
Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if impossible.
"""
def minimumSwap(s1: str, s2: str) -> int:
    
    xy_count = 0
    yx_count = 0
    for i in range(len(s1)):
        if(s1[i] == 'x' and s2[i] == 'y'):
           xy_count+=1
        elif(s1[i] == 'y' and s2[i] == 'x'):
           yx_count+=1
    if((xy_count + yx_count) % 2 == 1):
        return -1
    else:
        return xy_count/2 + yx_count/2 + ((xy_count)%2) + ((yx_count)%2)
    return -1

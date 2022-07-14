# Return the minimum number of swaps to make s balanced.


def minSwaps( s: str) -> int:
    minSwap = 0
    n = len(s)
    p1 = 0
    p2 = n - 1
    while(p1 < p2):
        if(s[p1] > s[p2]):
            s[p1] , s[p2] = s[p2], s[p1]
            minSwap +=1
            p1+=1
            p2 -=1

    return minSwaps


a = '['
b = ']'
if a > b:
     print(a)
else: print(b)
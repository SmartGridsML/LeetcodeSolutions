def recursive_longestCommonSubsequence(A : str , B : str ) -> int:
    LCR = 0
    if not A or not B:
        return 0
    if A[-1] == B[-1]:
        return 1 + recursive_longestCommonSubsequence(A[: -1] , B[: -1])
    return max(recursive_longestCommonSubsequence (A , B[:-1]) , 
                recursive_longestCommonSubsequence( A[:-1] , B))


def dpLCR(A : str , B : str ) -> int:
    m = len(A)
    n = len(B)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n  +1):
            if(A[i-1] == B[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                print("index", "[", i, "]", "[", j, "]", "value", dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
                print("index", "[", i, "]", "[", j, "]", "value" , dp[i][j])
    return dp[m ][ n]
    #print(dp)

def main():
    s1 = "abcdef"
    s2 = "acf"
    m = len(s1)
    n = len(s2)
    rLCR = recursive_longestCommonSubsequence(s1 , s2)
    dp_sol = dpLCR(s1, s2)
    print(f"LCR = {rLCR}")
    print(f"dpLCR = {dp_sol}")
    #dp = [[0] * n for i in range(m+1)]
    #print(dp)
    return rLCR 

if __name__ == '__main__':
    main()

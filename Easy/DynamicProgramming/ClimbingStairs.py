#You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs( n: int) -> int:
    dp = [0 for i in range(n+1)]
    dp[0] , dp[1]  = 1 , 1
    for i in range(2 , n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]


assert(climbStairs(44) == 1134903170)

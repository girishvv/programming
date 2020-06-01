# -*- coding: utf-8 -*-
#A child is running up a staircase with n steps and can hop either 1 step, 2 steps,
#or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
def nuberOfWays(n):
    if n==0:
        return 0
    dp = [0]*n
    
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3,n):
        dp[i] = 1 + dp[i-1] + dp[i-2] +dp[i-3]
    
    return dp[-1]

if __name__ == "__main__":
    n = 4
    print(nuberOfWays(n))
    


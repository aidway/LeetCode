'''
算法：动态规划。也可用矩阵快速幂解决。
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+2)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
         
        return dp[n]
        
        
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+2)]
        dp1 = 1
        dp2 = 2
        dpn = 0
        for i in range(3, n+1):
            dpn = dp1 + dp2
            dp1 = dp2
            dp2 = dpn 
         
        if n == 1:
            return dp1
        elif n == 2:
            return dp2
        else:
            return dpn
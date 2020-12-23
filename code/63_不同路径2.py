'''
算法：动态规划
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1] * n for i in range(m)]

        i = 0
        status = False
        while i < n:
            if obstacleGrid[0][i] == 1:
                status = True
            if status:
                dp[0][i] = 0
            i += 1

        i = 0
        status = False
        while i < m:
            if obstacleGrid[i][0] == 1:
                status = True
            if status:
                dp[i][0] = 0
            i += 1
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
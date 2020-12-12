'''
算法：动态规划。
dp[i][j] : s的前i个字符能否被p的前j个字符匹配。
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False] * (n+1)  for _ in range((m+1))]

        # 空能被空匹配
        dp[0][0] = True

        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]
                elif p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

        return dp[m][n]
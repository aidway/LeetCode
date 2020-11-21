'''
算法：动态规划
'''
class Solution:
    def matches(self, s, p ):
        if p == '.':
            return True
        else:
            return s == p

    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        '''
        f : (m+1) * (n+1) 矩阵
        f[i][j] : s[:i]能被p[:j] 匹配
        s = abc
        p = aaa
        f[1][1] = True
        原因：s[:1]=a p[:1]=a 能够匹配

        s=aa
        p=a*
        f[0][2] = True
        原因：s[:0] = '' p[:2]=a* 能够匹配
        '''
        f = [[False] * (n+1)  for _ in range((m+1))]
        # 空能被空匹配
        f[0][0] = True
        
        '''
        k > 0
        f[0][k] 可能为True，所以i要从0开始枚举
        f[k][0] 一定为False，非空的字符串不能被空的正则匹配，故j从1开始匹配
        '''
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] != '*':
                    if i > 0 and self.matches(s[i-1], p[j-1]):
                        f[i][j] = f[i-1][j-1]
                else:
                    if i > 0 and self.matches(s[i-1], p[j-2]):
                        f[i][j] = f[i-1][j] | f[i][j-2]
                    else:
                        f[i][j] =  f[i][j-2]
                
        return f[m][n]
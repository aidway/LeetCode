'''
算法：递归。枚举每一行。
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cur = [['.'] * n for i in range(n)]
        ans = []
        col = [False for i in range(n)]

        # 判断是否会有攻击
        def attach(r, c):
            # 检查列
            if col[c]:
                return True

            # 检查y=x
            r2, c2 = r, c
            while c2 > 0 and r2 > 0 :
                if cur[r2-1][c2-1] == 'Q':
                    return True
                r2 -= 1
                c2 -= 1

            # 检查y=-x
            r2, c2 = r, c  
            while c2 +1 < n and r2 > 0  :
                if cur[r2-1][c2+1] == 'Q':
                    return True
                r2 -= 1
                c2 += 1

            return False

        def dfs(r):
            if r == n:
                ans.append([''.join(i) for i in cur])
                return True
                
            # 枚举每一列
            for i in range(n):
                if not attach(r, i):
                    col[i] = True
                    cur[r][i] = 'Q'
                    dfs(r+1)
                    col[i] = False
                    cur[r][i] = '.'
            return False

        # 从第0行开始枚举
        dfs(0)
        return ans
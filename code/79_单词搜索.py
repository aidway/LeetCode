'''
算法：递归，深度优先搜索
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        nw = len(word)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        '''
        cur_ans: 当前解
        p_row: 当前所在行
        p_col: 当前所在列
        '''
        def dfs(cur_ans, p_row, p_col):
            k = len(cur_ans)
            if k == nw:
                return True

            for dr, dc in directions:
                newr, newc = p_row + dr, p_col + dc
                if newr >=0 and newr < n and newc >= 0 and newc < m:
                    if not visited[newr][newc] and  board[newr][newc] == word[k]:
                        visited[newr][newc] = True
                        res = dfs(cur_ans + [board[newr][newc]], newr, newc)
                        if res:
                            return True
                        visited[newr][newc] = False

            return False

        visited = [[False] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                # 找到与word中第一个字母相同的字母，作为起始点
                if board[r][c] == word[0]:
                    visited[r][c] = True
                    res = dfs([board[r][c]], r, c)
                    if res:
                        return True
                    visited[r][c] = False

        return False
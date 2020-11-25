'''
算法：哈希
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        sub_sudo = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    tmp = int(board[i][j])
                    sub_sudo_idx = (i // 3) * 3 + j // 3

                    # 行
                    if row[i].get(tmp, 0) > 0:
                        return False
                    else:
                        row[i][tmp] = 1

                    # 列
                    if col[j].get(tmp, 0) > 0:
                        return False
                    else:
                        col[j][tmp] = 1

                    # 子数独
                    if sub_sudo[sub_sudo_idx].get(tmp, 0) > 0:
                        return False
                    else:
                        sub_sudo[sub_sudo_idx][tmp] = 1
        return True

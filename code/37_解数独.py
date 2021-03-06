'''
�㷨���ݹ�
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # ״̬��ʼ��
        N = 9
        row = [{} for i in range(N)]
        col = [{} for i in range(N)]
        sub = [{} for i in range(N)]
        for i in range(N):
            for j in range(N):
                sub_idx = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row[i][num] = 1
                    col[j][num] = 1
                    sub[sub_idx][num] = 1
                    
        # ȫ��״̬            
        status = False
        def dfs(r, c):
            nonlocal status
            if board[r][c] != '.':
                if c + 1 < N:
                    dfs(r, c + 1)
                elif r + 1 < N:
                    dfs(r + 1, 0)
                else:
                    status = True
                    return True
            
            else:
                sub_idx = (r // 3 * 3) + c // 3
                for k in range(1, 10):
                    if row[r].get(k, 0) == 0 and col[c].get(k, 0) == 0 and sub[sub_idx].get(k, 0) == 0:
                        # ���Է�������
                        board[r][c] = str(k)
                        row[r][k] = 1
                        col[c][k] = 1
                        sub[sub_idx][k] = 1
                        
                        # �ݹ�
                        if r == N - 1 and c == N - 1:
                            status = True
                            return True
                        elif c + 1 < N  :
                            dfs(r, c + 1)
                        elif r + 1 < N  :
                            dfs(r + 1, 0)
                        
                        # �жϽ��
                        if status:
                            return True
                        else:
                            board[r][c] = '.'
                            row[r][k] = 0
                            col[c][k] = 0
                            sub[sub_idx][k] = 0
                        
                       

                return False

        dfs(0, 0)

 
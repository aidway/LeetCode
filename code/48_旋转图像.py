'''
算法：先转置，后将每一行逆转
'''

import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])

        # 矩阵转置
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 行逆
        for i in range(n):
            matrix[i].reverse()
        
 
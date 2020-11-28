import numpy as np


class Solution:
    def rotate(self ) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
        matrix = np.array(matrix)
        n = len(matrix)
        print(n)
        k = n // 2
        for i in range(k):
            # 第一行
            # print(matrix[i:i + 1].reshape(3, ))
            # 右侧列
            # print(matrix[:, n - k])
            # 最后一行
            # print(matrix[n - k:].reshape(3, ))
            # 第一列
            # print(matrix[:, i])

            a = matrix[i,i:n-i].reshape(n-i*k, ).copy()
            b = matrix[i:n-i, n - i-1][::-1].copy()
            c = matrix[n - i-1,i:n-i].reshape(n-i*k, ).copy()
            d = matrix[i:n-i:, i][::-1].copy()

            matrix[i:n - i, n - i - 1] = a
            # # print(matrix)
            matrix[n - i - 1, i:n - i] = b
            # # print(matrix)
            matrix[i:n - i:, i] = c
            # # print(matrix)
            matrix[i,i:n-i] = d
        # print(matrix)

        return matrix

sol = Solution()
print(sol.rotate( ))
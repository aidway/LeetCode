'''
�㷨��ģ��
'''
import numpy as np
import math
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = np.array(matrix)
        m = arr.shape[0]
        n = arr.shape[1]
        k = min (math.ceil(m/2),math.ceil(n/2))
        ans = []

        for i in range(k):
            # ����
            ans.extend(arr[i,i:n-i].tolist())
            # ����
            ans.extend(arr[i+1:m-i-1,n-i-1].tolist())
            # ����
            if m-i-1 > i:
                ans.extend(arr[m-i-1,i:n-i][::-1].tolist())
            # ����
            if n-i-1 > i:
                ans.extend(arr[i+1:m-i-1, i][::-1].tolist())

        return ans
        
        
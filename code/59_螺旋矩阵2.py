'''
�㷨��ģ��
'''
import numpy as np
import math
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        k = math.ceil(n/2)
        v = 1
        arr = np.full((n,n), 0)
        k = math.ceil(n/2)
      
        for i in range(k):
            # ����
            tmp = []
            for j in range(i, n-i):
                tmp.extend([v])
                v += 1
            arr[i,i:n-i] = tmp
            # ����
            tmp = []
            for j in range(i+1, n-i-1):
                tmp.extend([v])
                v += 1
            arr[i+1:n-i-1,n-i-1] = tmp
            # ����
            tmp = []
            if n-i-1 > i:
                for j in range(i, n-i):
                    tmp.extend([v])
                    v += 1
                arr[n-i-1,i:n-i][::-1] = tmp
            # ����
            tmp = []
            if n-i-1 > i:
                for j in range(i+1, n-i-1):
                    tmp.extend([v])
                    v += 1
                arr[i+1:n-i-1, i][::-1] = tmp

        return arr.tolist()
        
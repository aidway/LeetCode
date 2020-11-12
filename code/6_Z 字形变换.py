'''
算法：模拟。
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        slen = len(s)
        ans = [[] * (slen // numRows + 1) for i in range(numRows)]

        k = 1
        p = 0
        while p < slen:
            # 向下走
            if k % 2 == 1:
                j = 0
                for i in range(numRows):
                    if p+i < slen:
                        ans[i].append(s[p+i])
                        j = j + 1
                p = p + j
            # 向上走
            else:
                j = 0
                for i in range(numRows - 2, 0, -1):
                    if p+ numRows - 2 - i < slen:
                        ans[i].append(s[p+ numRows - 2 - i])
                        j = j + 1
                p = p + j
                
            k = k + 1
           
        ans_s =''
        for i in ans:
            ans_s = ans_s + ''.join(i)
        return ans_s
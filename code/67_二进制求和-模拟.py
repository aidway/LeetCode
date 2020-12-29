'''
算法：模拟
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        
        ans = ['']

        c = 0
        a = a[::-1]
        b = b[::-1]
        n = len(a)
        m = len(b)
        for i in range(n):
            t = int(a[i]) + c
            if i < m:
                t +=   int(b[i]) 
            
            c = t // 2
            ans.append(str(t%2))
        
        if c == 1:
            ans.append(str(1))

        return ''.join(ans)[::-1]


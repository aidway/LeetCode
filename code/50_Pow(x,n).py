'''
Ëã·¨£º·ÖÖÎ
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1         
        
        def go(m):
            if m == 0 :
                return 1
            v = go(m // 2)

            return v * v if m % 2 == 0 else  v * v * x
         
        return go(n) if n >= 0 else 1.0 / go(-n)
        
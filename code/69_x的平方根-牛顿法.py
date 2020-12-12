'''
算法：牛顿法
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C = x
        x0 = C
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(xi - x0) < 1e-7:
                break
            x0 = xi
          
        return int(x0)
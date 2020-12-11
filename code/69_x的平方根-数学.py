'''
算法：数学
'''
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans =  int(math.exp(0.5 * math.log(x)))
        
        return ans+1 if (ans+1)**2 <= x else ans



'''
算法：递归。加倍后迭代逼近。
'''
class Solution:
    def run(self, dividend: int, divisor: int):
        bit = divisor
        ans = 1
        while bit + bit <= dividend:
            bit = bit + bit
            ans = ans + ans
        
        dividend = dividend - bit
        if dividend >= 0:
            return self.divide(dividend, divisor) + ans
        else:
            return 0


    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)
        
        flag = 1
         
        if dividend > 0 and divisor < 0:
            flag = -1
            divisor = -divisor
        elif dividend < 0 and divisor > 0:
            flag = -1
            dividend = -dividend
        elif dividend < 0 and divisor < 0:
            divisor = -divisor
            dividend = -dividend
                
        ans = self.run(dividend, divisor)
        if flag == -1:
            ans = -ans
        if ans < INT_MIN or ans > INT_MAX:
            ans = INT_MAX

        return ans
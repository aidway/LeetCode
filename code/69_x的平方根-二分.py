'''
算法：二分查找
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        mid = 0
        while left <= right:
            mid = (left + right ) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else :
                left = mid + 1
                ans = mid        
        return ans



'''
算法：贪心
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxj = 0
        for i in range(n-1):
            # 如果不能跳过0
            if nums[i] == 0 and maxj < i + 1:
                return False

            if maxj < nums[i] + i:
                maxj = nums[i] + i
             
            if maxj >= n - 1:
                return True
        return n == 1
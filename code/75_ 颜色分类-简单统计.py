'''
算法：简单统计
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0, c1, c2 = 0, 0, 0

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1
            else:
                c2 += 1
        
        nums[0:c0] = [0] * c0
        nums[c0:c1+c0] = [1] * c1
        nums[c0+c1:] = [2] * c2
        
'''
Ëã·¨£ºÄ£Äâ¡£
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            if nums[i] == target:
                return i
            elif nums[i] > target and ans == -1:
                ans = i
        return ans if ans != -1 else n

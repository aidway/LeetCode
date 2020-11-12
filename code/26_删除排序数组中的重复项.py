'''
Ëã·¨£ºÄ£Äâ
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        p = 0
        while i < n:
            while i+1 < n and nums[i] == nums[i+1]:
                i = i + 1
            
            if i+1 < n :
                nums[p+1] = nums[i+1]
                p = p + 1
            i = i + 1
        return p+1
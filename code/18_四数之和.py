'''
算法：枚举+双向指针
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left = left + 1
                        while left < right and nums[left] == nums[left - 1]:
                            left = left + 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right = right - 1
                    else:
                        left = left + 1
                    
                    if left == right:
                        break
        return ans
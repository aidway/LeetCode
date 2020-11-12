'''
算法：枚举+双向指针
1. 将数组升序排序
2. 枚举数组中的每一个数字，记当前已枚举到nums[i]，对nums[i+1,len(nums)]进行二次枚举。
记left=i+1，right=len(nums)，根据nums[i]+nums[left]+nums[right]与0的关系，移动left或right。
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n -1 
            while left < right:
                while left < right and nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                while left < right and nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
                if right == left:
                    break
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 找到一组解时，应继续移动左或右指针进行枚举
                    left = left + 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    left = left + 1
        return ans
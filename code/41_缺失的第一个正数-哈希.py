'''
算法：原地哈希。设数组长度为N，那么解一定在[1,N+1]之间。设整数p应该在nums[p-1]位置，若不在，让它去该去的地方。
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # 当nums[i]不在其位时进行交换，让它去该去的地方
            while  nums[i] > 0 and nums[i]-1 < n and nums[i] != nums[nums[i] - 1] :
                p = nums[i] - 1
                nums[i], nums[p] = nums[p], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

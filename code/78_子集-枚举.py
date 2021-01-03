'''
算法：枚举
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        print(1<<n)

        total = 1<<n
        for mask in range(total):
            cur_ans = []
            for i in range(n):
                if mask & (1<<i):
                    cur_ans.append(nums[i])
            
            ans.append(cur_ans.copy())

        return ans
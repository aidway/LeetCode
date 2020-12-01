'''
算法：递归
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ans = []
        
        '''
        p: 当前位置
        left_nums: 剩余可选择的元素
        cur_ans: 当前解
        '''
        def dfs(p, left_nums, cur_ans):
            n = len(left_nums)
            i = 0
            while i < n:
                if p == len(nums) - 1:
                    ans.append(cur_ans+[left_nums[i]])
                else:
                    while i > 0 and i < n and left_nums[i] == left_nums[i-1]:
                        i += 1
                    if i < n:
                        dfs(p+1, left_nums[:i]+left_nums[i+1:], cur_ans+[left_nums[i]])
                i += 1

        dfs(0, nums, [])
        return ans
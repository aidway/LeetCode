'''
算法：递归
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cnt = len(nums)
        ans = []

        '''
        p: 当前位置
        left_nums: 剩余可选择的元素
        cur_ans: 当前解
        '''
        def dfs(p, left_nums, cur_ans):
            n = len(left_nums)

            # 枚举每个可选择的元素
            for i in range(n):
                t = left_nums[i]
                if p == cnt - 1:
                    ans.append(cur_ans + [t])
                else:
                    tmp_ls = left_nums[:i] + left_nums[i+1:]
                    dfs(p+1, tmp_ls, cur_ans+[t])
        
        dfs(0, nums, [])

        return ans

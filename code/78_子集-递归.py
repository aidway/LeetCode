'''
算法：递归
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        # p: 当前枚举起点
        # cur_ans: 当前解
        def  dfs(p, cur_ans):
            ans.append(cur_ans)
            for i in range(p, n):
                dfs(i+1, cur_ans+[nums[i]])

        dfs(0, [])

        return ans
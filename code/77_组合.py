'''
算法：递归
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(p, cur_ans):
            if len(cur_ans) == k:
                ans.append(cur_ans)
                return

            for i in range(p, n + 1):
                dfs(i + 1, cur_ans+[i])

        dfs(1,[])

        return ans
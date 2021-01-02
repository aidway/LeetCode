class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur_ans = []

        def dfs(p):
            if len(cur_ans) == k:
                # 如果不copy，ans也会被pop
                ans.append(cur_ans.copy())
                return

            for i in range(p, n + 1):
                cur_ans.append(i)
                dfs(i + 1)
                cur_ans.pop()

        dfs(1)

        return ans
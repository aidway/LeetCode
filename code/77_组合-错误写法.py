class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur_ans = []

        def dfs(p, cur_ans):
            if len(cur_ans) == k:
                ans.append(cur_ans)
                return

            for i in range(p, n + 1):
                cur_ans.append(i)
                dfs(i + 1, cur_ans+[i])
                cur_ans.pop()

        dfs(1,[])
        print(ans)


sol = Solution()
print(sol.combine(4,2  ))

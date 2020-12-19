'''
算法：递归
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:         
        ans = ['' for i in range(n )]

        f = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            f[i] = f[i - 1] * i

        used = [False for i in range(n + 1)]

        '''
        ans_num: 当前已放置数字的个数
        '''
        def dfs(k, ans_num):
            if ans_num == n:
                return
            s = f[n - ans_num - 1]

            # 寻找位置 ans_num 可以放置的数字
            v = math.ceil(k / s)
            i = 1
            cnt = 0
            while cnt < v:
                if not used[i]:
                    cnt += 1
                i += 1
            used[i-1] = True
            ans[ans_num] = str(i-1)
            dfs(k - (v-1) * s, ans_num + 1)

        dfs(k, 0)
        return ''.join(ans[:])

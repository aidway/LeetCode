'''
算法：模拟
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        t = [i for i in range(n+1)]
        ans = ['' for i in range(n+1)]
        f = [0 for i in range(n+1)]
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] * i

        for i in range(1, n+1):
            p = n - i
            # 如果仅剩最后一个数字，直接放之
            if p == 0:
                ans[i] = str(t[1])
                break
            j = 1
            # 尝试在第i个位置，可以放第几个数字
            while True:
                if j * f[p] >= k:
                    break
                j += 1
            ans[i] = str(t[j])
            k = k - (j-1) * f[p]
            t.pop(j)

        return ''.join(ans[1:])

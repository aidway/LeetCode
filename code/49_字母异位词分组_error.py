class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        ans = []
        for i in range(n):
            k = len(ans)
            if k == 0:
                ans.append([strs[i]])
                continue
            j = 0
            s = strs[i][::-1]
            # print(ans)
            while j < k:
                if sorted(ans[j][0][::-1]) == sorted(s):
                    print(s)
                    ans[j].extend([strs[i]])
                    break
                j += 1
            if j >= k:
                ans.append([strs[i]])

        return ans

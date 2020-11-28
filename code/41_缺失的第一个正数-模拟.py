'''
算法：模拟。已知正整数nums[i]，可能的解为nums[i]-1或nums[i]+1
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = set()
        n = len(nums)
        i = 0
        d = {}
        while i < n:
            if nums[i] == 1 :
                if d.get(2,0) == 0:
                    ans.add(2)
                d[nums[i]] = 1
                ans.discard(nums[i])
            elif nums[i] > 1:
                a = nums[i] - 1
                b = nums[i] + 1
                if d.get(a,0) == 0 :
                    ans.add(a)
                if d.get(b,0) == 0:
                    ans.add(b)
                ans.discard(nums[i])
                d[nums[i]] = 1
            i += 1

        if d.get(1,0) == 0:
            return 1
        return min(ans)
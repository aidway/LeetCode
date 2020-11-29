'''
算法：动态规划。dp[i]为以i结尾的最大子数组和，则 dp[i+1] = max(dp[i] + nums[i], nums[i])， 最终结果为max(dp)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums[0]
        ans = nums[0]
        for i in range(1, n):
            dp = max(dp + nums[i],nums[i])

            if dp > ans:
                ans = dp

        return ans
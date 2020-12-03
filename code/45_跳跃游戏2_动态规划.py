'''
算法：动态规划
'''
class Solution:
    def jump(self, nums: List[int]) -> int:        
        n = len(nums)
        if n == 1:
            return 0
        dp = [999999999 for i in range(n)]
        dp[0] = 0  # dp[i] = j，到达点i需要跳跃j次
        maxj = 0   # 当前已跳跃的最远位置
        # 枚举起始点i
        for i in range(n):
            # 枚举起始点i的跳跃次数
            for j in range(nums[i], 0, -1):
                '''
                剪枝：
                i+j为从点i可以跳跃到达的位置，如果该位置曾经到达过，无需再跳跃
                例如：[3,2,1]，从0点可以到达位置2，则无需从1点到达2，因为会多跳一次
                '''
                if i + j < maxj:
                    break
                
                # 到达终点
                if i + j >= n-1:
                    return dp[i] + 1
                elif dp[i + j] > dp[i] + 1:
                    dp[i + j] = dp[i] + 1
                    
            if maxj < i + nums[i]:
                maxj = i + nums[i]
                 
        return dp[n-1]
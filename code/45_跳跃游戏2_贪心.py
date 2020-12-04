'''
算法：贪心。对[2,3,1,1,4]，0点最远可以跳到2点，所以在[1,2]之间，仅需一跳。那么从[1,2]出发，最远能够跳到的位置，就是第二跳的终点。
'''
class Solution:
    def jump(self, nums: List[int]) -> int:        
        n = len(nums)
         
        maxj = 0   # 当前已跳跃的最远位置
        step = 0
        cur_end = 0  # 当前终点
        # 枚举起始点i
        for i in range(n-1):
            if i + nums[i] > maxj:
                maxj = i + nums[i]
                
            # 到达下一次起跳点
            if i == cur_end:
                step += 1
                cur_end = maxj
                 
        return step
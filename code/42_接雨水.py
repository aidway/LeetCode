'''
算法：模拟
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        ans = 0
        while i < n - 1:
            if height[i] == 0:
                i += 1
                continue

            left = i
    
            # 寻找 >=左柱 的 右柱
            while i+1 < n and height[i+1] < height[left]:
                i += 1
                
            if i + 1 < n :
                # 如果 右柱 >= 左柱，说明[左柱，右柱]之间恰好可以接雨水
                right = i + 1
                h = min(height[left], height[right])
                for j in range(left, right):
                    ans += max(h-height[j] ,0)
                    j += 1
                #i = right 
            else:
                # 如果没有比左柱更高的右柱，则从最右侧开始寻找最高的柱子，该柱为当前的右柱
                i = left
                maxnum_h = -1
                maxnum_p = 0
                for j in range(n-1, i, -1):
                    if height[j] > maxnum_h:
                        maxnum_h = height[j]
                        maxnum_p = j
                right = maxnum_p
                h = min(height[left], height[right])
                for j in range(left, right+1):
                    ans += max(h-height[j] ,0)
                    j += 1
            i = right
             


        return ans
            
'''
算法：贪心。使用首尾双指针，每次移动高度较低的指针，可能会获得更大的容量。
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = -1 
        while i < j:
            if (j-i) * min(height[i], height[j]) > ans:
                ans = (j-i) * min(height[i], height[j])
                
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ans
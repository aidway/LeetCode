'''
�㷨��̰�ġ�ʹ����β˫ָ�룬ÿ���ƶ��߶Ƚϵ͵�ָ�룬���ܻ��ø����������
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
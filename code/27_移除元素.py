'''
�㷨��ģ�⡣����ָ��p��p������ݲ�����val���������ݣ������ݲ�����valʱ�������ݷŵ�λ��p��ͬʱp���ơ�
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != val:
                nums[p] = nums[i]
                p = p + 1
            i = i + 1
        return p 

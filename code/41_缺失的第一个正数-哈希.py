'''
�㷨��ԭ�ع�ϣ�������鳤��ΪN����ô��һ����[1,N+1]֮�䡣������pӦ����nums[p-1]λ�ã������ڣ�����ȥ��ȥ�ĵط���
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # ��nums[i]������λʱ���н���������ȥ��ȥ�ĵط�
            while  nums[i] > 0 and nums[i]-1 < n and nums[i] != nums[nums[i] - 1] :
                p = nums[i] - 1
                nums[i], nums[p] = nums[p], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

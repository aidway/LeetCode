'''
�㷨��̰��
1���ҵ��ɽ��������λ����12453����2��3������13452����Ϳɽ�����Ϊ��λ�ϵ�2
2������1���������λ������е�������
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ok = False
        ans = -1
        
        # �ҵ������������λ
        for i in range(n-2,-1,-1):
            for j in range(n-1, i, -1):
                if nums[j] > nums[i]:
                    ans = i
                    nums[j] , nums[i] = nums[i], nums[j]
                    ok = True
                    break
            if ok:
                break
                
        if ok:
            # ���λ�������������
            for i in range(ans+1, n):
                for j in range(i+1, n):
                    if   nums[j] < nums[i]:
                        nums[j] , nums[i] = nums[i], nums[j]
        else:
            # list��ת���������У�
            for i in range(int(n/2)):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
        
        
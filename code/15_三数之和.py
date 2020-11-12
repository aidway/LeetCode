'''
�㷨��ö��+˫��ָ��
1. ��������������
2. ö�������е�ÿһ�����֣��ǵ�ǰ��ö�ٵ�nums[i]����nums[i+1,len(nums)]���ж���ö�١�
��left=i+1��right=len(nums)������nums[i]+nums[left]+nums[right]��0�Ĺ�ϵ���ƶ�left��right��
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n -1 
            while left < right:
                while left < right and nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                while left < right and nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
                if right == left:
                    break
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    # �ҵ�һ���ʱ��Ӧ�����ƶ������ָ�����ö��
                    left = left + 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    left = left + 1
        return ans
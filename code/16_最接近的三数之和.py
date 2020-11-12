'''
�㷨��ö��+˫��ָ�롣
1.��nums��������
2.���赱ǰ��ö�ٵ�nums[i]=a��Ȼ���ٶ�nums[i+1,n]����ö�١�
��left=i+1��right=n-1
���nums[i]+nums[left]+nums[right]>target����right=right-1������Ϊ���������У������left�����ƶ�����ͻ��target����
���nums[i]+nums[left]+nums[right]<target����left=left+1
���nums[i]+nums[left]+nums[right]=target���򷵻�target
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        v  = 999999
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n -1 
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    return target
                elif nums[i] + nums[left] + nums[right] > target:
                    '''
                    ���nums=[-1,1,2],target=1����ʱ-1+1+2>target��������ѭ��ǰ����Ҫ���ж�-1+1+2�Ƿ������Ž�
                    '''
                    if abs(nums[i] + nums[left] + nums[right] - target ) < v:
                        v = abs(nums[i] + nums[left] + nums[right] - target )
                        ans = nums[i] + nums[left] + nums[right]
                    right = right - 1
                else:
                    if abs(nums[i] + nums[left] + nums[right] - target ) < v:
                        v = abs(nums[i] + nums[left] + nums[right] - target )
                        ans = nums[i] + nums[left] + nums[right]
                    left = left + 1
                                        
                if left < right and abs(nums[i] + nums[left] + nums[right] - target ) < v:
                    v = abs(nums[i] + nums[left] + nums[right] - target )
                    ans = nums[i] + nums[left] + nums[right]

        return ans
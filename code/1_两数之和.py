class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        �㷨��ö��ÿ�����֣���maps�������ֵ����ͣ���¼ÿ��������Ҫ�ĸ����ֿ������ƥ��
        '''
        
        '''
        maps[key] = value
        key:����Ҫ������
        value:��˭��Ҫ�����ֵ�index
        ���ӣ�
        maps[2] = 1
        ����2��nums[1]��Ҫ���� 2 + nums[1] = target
        '''
        maps = {}
        ind = 0
        for n1 in nums:
            n2 = target - n1
            
            # ���n1����Ҫ��
            if n1 in maps.keys() :
                return [maps[n1],ind]
                
            # n2 �� nums[ind]��Ҫ
            maps[n2] = ind
            
            ind += 1
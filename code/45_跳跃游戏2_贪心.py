'''
�㷨��̰�ġ���[2,3,1,1,4]��0����Զ��������2�㣬������[1,2]֮�䣬����һ������ô��[1,2]��������Զ�ܹ�������λ�ã����ǵڶ������յ㡣
'''
class Solution:
    def jump(self, nums: List[int]) -> int:        
        n = len(nums)
         
        maxj = 0   # ��ǰ����Ծ����Զλ��
        step = 0
        cur_end = 0  # ��ǰ�յ�
        # ö����ʼ��i
        for i in range(n-1):
            if i + nums[i] > maxj:
                maxj = i + nums[i]
                
            # ������һ��������
            if i == cur_end:
                step += 1
                cur_end = maxj
                 
        return step
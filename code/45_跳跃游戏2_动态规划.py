'''
�㷨����̬�滮
'''
class Solution:
    def jump(self, nums: List[int]) -> int:        
        n = len(nums)
        if n == 1:
            return 0
        dp = [999999999 for i in range(n)]
        dp[0] = 0  # dp[i] = j�������i��Ҫ��Ծj��
        maxj = 0   # ��ǰ����Ծ����Զλ��
        # ö����ʼ��i
        for i in range(n):
            # ö����ʼ��i����Ծ����
            for j in range(nums[i], 0, -1):
                '''
                ��֦��
                i+jΪ�ӵ�i������Ծ�����λ�ã������λ���������������������Ծ
                ���磺[3,2,1]����0����Ե���λ��2���������1�㵽��2����Ϊ�����һ��
                '''
                if i + j < maxj:
                    break
                
                # �����յ�
                if i + j >= n-1:
                    return dp[i] + 1
                elif dp[i + j] > dp[i] + 1:
                    dp[i + j] = dp[i] + 1
                    
            if maxj < i + nums[i]:
                maxj = i + nums[i]
                 
        return dp[n-1]
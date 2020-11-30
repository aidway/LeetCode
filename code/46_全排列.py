'''
�㷨���ݹ�
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cnt = len(nums)
        ans = []

        '''
        p: ��ǰλ��
        left_nums: ʣ���ѡ���Ԫ��
        cur_ans: ��ǰ��
        '''
        def dfs(p, left_nums, cur_ans):
            n = len(left_nums)

            # ö��ÿ����ѡ���Ԫ��
            for i in range(n):
                t = left_nums[i]
                if p == cnt - 1:
                    ans.append(cur_ans + [t])
                else:
                    tmp_ls = left_nums[:i] + left_nums[i+1:]
                    dfs(p+1, tmp_ls, cur_ans+[t])
        
        dfs(0, nums, [])

        return ans

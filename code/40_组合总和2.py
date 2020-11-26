'''
�㷨���ݹ�
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)
        ans = []
        '''
        p: ��ǰ���Ե����
        cur_ans: ��ǰ��
        left_target: ʣ���ܺ�
        '''
        def dfs(p, cur_ans, left_target):
            while p < n:
                status = False
                if candidates[p] == left_target:
                    cur_ans.extend([candidates[p]])
                    ans.append(cur_ans)
                    return True
                elif candidates[p] < left_target:
                    # ��ֹ����[1,5,2]���ֽ�
                    if left_target - candidates[p] >= candidates[p]:
                        dfs(p+1, cur_ans + [candidates[p]], left_target - candidates[p])
                        
                # �����ظ�����
                while  p+1 < n and candidates[p] == candidates[p+1]:
                    p += 1
                p += 1

        dfs(0, [], target)
        return ans
'''
�㷨������
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        '''
        p: ��ǰ����������λ��
        combine: ��ǰ���
        t: ��ǰ��target
        '''
        def dfs(p, combine, t):
            for i in range(p, len(candidates)):
                if candidates[i] == t:
                    ans.append(combine + [candidates[i]])
                elif candidates[i] < t:
                    dfs(i, combine + [candidates[i]], t - candidates[i])
                else:
                    return

        dfs(0, [], target)
        return ans
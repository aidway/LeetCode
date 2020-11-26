'''
算法：递归
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)
        ans = []
        '''
        p: 当前尝试的起点
        cur_ans: 当前解
        left_target: 剩余总和
        '''
        def dfs(p, cur_ans, left_target):
            while p < n:
                status = False
                if candidates[p] == left_target:
                    cur_ans.extend([candidates[p]])
                    ans.append(cur_ans)
                    return True
                elif candidates[p] < left_target:
                    # 防止出现[1,5,2]这种解
                    if left_target - candidates[p] >= candidates[p]:
                        dfs(p+1, cur_ans + [candidates[p]], left_target - candidates[p])
                        
                # 跳过重复数字
                while  p+1 < n and candidates[p] == candidates[p+1]:
                    p += 1
                p += 1

        dfs(0, [], target)
        return ans
'''
算法：官方
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        intervals = sorted((intervals))

        # i = 0
        ans = [intervals[0]]
        for i in range(1, n):
            # 无交集
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        

        return ans


 
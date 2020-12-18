'''
算法：贪心。转化为T56-合并区间。
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)

        # 如果interval为空
        if n == 0:
            return [newInterval]

        # 将newInterval合并到interval
        i = 0
        while i < n:
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break
            i += 1
        if i >=n:
            intervals.append(newInterval)

        # 合并
        ans.append(intervals[0])
        for i in range(1, n+1):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans
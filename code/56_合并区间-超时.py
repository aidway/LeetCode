'''
算法：模拟。超时了！！！
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [0,0]
        n = len(intervals)
        j = 0
        while j < len(intervals):
            tmp = intervals[j]
            status = False
            i = j + 1
            while i < len(intervals):
                if not (tmp[0] > intervals[i][1] or intervals[i][0] > tmp[1]):
                    status = True
                    intervals[i][0] = min(tmp[0], intervals[i][0])
                    intervals[i][1] = max(tmp[1], intervals[i][1])
                i += 1
            if status:
                intervals.remove(tmp)
            else:
                j += 1

        return intervals

  
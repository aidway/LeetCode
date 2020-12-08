'''
算法：模拟
1、先按照左侧区间升序排序
2、判断前后两个区间是否重合，若重合，需要对后一个区间的最大值进行更新，取前后两个区间最大的右侧值
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        intervals = sorted((intervals))

        i = 0
        while i < n:
            j = i + 1
            right = intervals[i][0]
            left = intervals[i][1]
            while j < n:
                if j < n and not (intervals[j][0] > intervals[j-1][1] or intervals[j-1][0] > intervals[j][1]) :
                    left = max(left, intervals[j][1],intervals[j-1][1])
                    # 对后面区间的值进行更新
                    intervals[j][1] = max(intervals[j][1],intervals[j-1][1])
                    j += 1
                else:
                    break
            if j - i > 1:
                ans.append([intervals[i][0], left])
                i = j 
            else:
                ans.append(intervals[i])
                i += 1

        return ans


 
'''
算法：模拟
left <---> right
li   <---> ri
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        # 插入区间的起始
        left, right = newInterval[0], newInterval[1]

        placed = False
        for li, ri in intervals:
            if li > right:
                # [left,right] [li,ri]
                if not placed:
                    placed = True
                    ans.append([left, right])
                ans.append([li, ri])
            elif ri < left:
                # [li,ri] [left,right]
                ans.append([li, ri])
            else:
                # 有交集，更新插入区间范围
                left = min(li, left)
                right = max(ri, right)
        
        if not placed:
            ans.append([left, right])

        return ans
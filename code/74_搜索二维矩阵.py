'''
算法：二分枚举，先枚举行，后枚举列
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m - 1

        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target or matrix[mid][n-1] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][n-1] < target:
                left = mid + 1
            else:
                left = mid
                break

        left2 = 0
        right2 = n - 1
        while left2 <= right2:
            mid2 = (left2 + right2) // 2
            if matrix[left][mid2] == target:
                return True
            elif matrix[left][mid2] > target:
                right2 = mid2 - 1
            else:
                left2 = mid2 + 1

       
        return False
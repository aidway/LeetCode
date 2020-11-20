'''
算法：二分搜索
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1

        ans_left = 9999999999
        ans_right = -1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                ans_left = min(ans_left, mid)
                ans_right = max(ans_right, mid)

                if nums[right] == target and right != mid:
                    ans_right = max(ans_right, right)
                
                if nums[left] == target and left != mid:
                    ans_left = min(ans_left, left)

                right = right - 1
                left = left + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # 当不存在时，ans_right=-1
        return [min(ans_right,ans_left), ans_right]
       
       
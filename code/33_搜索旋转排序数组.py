'''
Ëã·¨£º¶þ·ÖËÑË÷
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # ÓÒ²àÉýÐò
            if nums[mid] < nums[right]:
                # ÔÚÓÒ²à
                if nums[mid] < target and target <= nums[right] :
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # ×ó²àÉýÐò
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

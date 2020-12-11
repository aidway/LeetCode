'''
算法：模拟。需要借用同nums1相同大小的数组。
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums3[i] < nums2[j]:
                nums1[k] = nums3[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
            
        for v in range(i, m):
            nums1[k] = nums3[v]
            k += 1
            
        for v in range(j, n):
            nums1[k] = nums2[v]
            k += 1
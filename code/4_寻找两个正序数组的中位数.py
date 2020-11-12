INT_MAX = float("inf")
INT_MIN = float("-inf")

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        
        if len1 == 0:
            return (nums2[int(len2/2)] + nums2[int((len2-1)/2)])/2.0
        
        if (len1 > len2):
            return self.findMedianSortedArrays(nums2, nums1)
                
        left = 0
        right = len1 * 2
        while (left <= right):
            c1 = int((left + right) / 2)
            c2 = len1 + len2 - c1

            L1 = INT_MIN if c1 == 0 else  nums1[int((c1 -1 ) / 2)]
                
            R1 = INT_MAX if c1 == len1 * 2 else nums1[int(c1/2)]
                
            L2 = INT_MIN if c2 == 0 else nums2[int((c2 -1 ) / 2)]
                
            R2 = INT_MAX if c2 == len2 * 2  else  nums2[int(c2/2)]
                
            if L1 > R2:
                right = c1 - 1
            elif L2 > R1:
                left = c1 + 1
            else:
                break
                
        return (max(L1,L2) + min(R1,R2)) / 2.0
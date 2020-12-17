'''
算法：转化为求两个数组第k大的数，进而使用二分搜索处理。
在nums1数组取 A = nums1[m//2-1]，则0-A共有m//2个数
在nums2数组取 B = nums2[n//2-1]，则0-B共有n//2个数
所以，0-A + 0-B 共有 (m+n)//2 个数，即中位数。（暂不考虑奇偶问题）
如果 A < B，则点A最大是第k-1的大数，即 .....AB 形式，因此，nums1中的0-A都不会是符合条件的点，可以去掉
如果 A > B，类似
如果 A = B，归入第一种情况
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            index1 = 0
            index2 = 0

            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newindex1 = min(index1+k//2-1, m-1)
                newindex2 = min(index2+k//2-1, n-1)
                if nums1[newindex1] <= nums2[newindex2]:
                    k = k - (newindex1 - index1 + 1)
                    index1 = newindex1 + 1
                else:
                    k = k - (newindex2 - index2 + 1)
                    index2 = newindex2 + 1

        m, n = len(nums1), len(nums2)
        if (m+n) % 2 == 1:
            return getKthElement((m+n+1) // 2)
        else:
            return (getKthElement((m+n)//2) + getKthElement((m+n)// 2 + 1)) / 2
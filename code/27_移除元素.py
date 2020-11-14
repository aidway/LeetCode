'''
算法：模拟。定义指针p，p左侧数据不等于val。遍历数据，当数据不等于val时，将数据放到位置p，同时p右移。
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != val:
                nums[p] = nums[i]
                p = p + 1
            i = i + 1
        return p 

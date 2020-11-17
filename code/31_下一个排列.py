'''
算法：贪心
1、找到可交换的最低位，如12453，将2和3交换后，13452，最低可交换的为万位上的2
2、步骤1交换后，最低位后的序列倒序排列
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ok = False
        ans = -1
        
        # 找到待交换的最低位
        for i in range(n-2,-1,-1):
            for j in range(n-1, i, -1):
                if nums[j] > nums[i]:
                    ans = i
                    nums[j] , nums[i] = nums[i], nums[j]
                    ok = True
                    break
            if ok:
                break
                
        if ok:
            # 最低位后的做降序排列
            for i in range(ans+1, n):
                for j in range(i+1, n):
                    if   nums[j] < nums[i]:
                        nums[j] , nums[i] = nums[i], nums[j]
        else:
            # list反转（倒序排列）
            for i in range(int(n/2)):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
        
        
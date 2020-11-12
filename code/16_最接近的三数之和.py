'''
算法：枚举+双向指针。
1.对nums升序排序
2.假设当前已枚举到nums[i]=a，然后再对nums[i+1,n]进行枚举。
令left=i+1，right=n-1
如果nums[i]+nums[left]+nums[right]>target，则right=right-1。（因为是升序排列，如果将left向右移动，求和会比target更大）
如果nums[i]+nums[left]+nums[right]<target，则left=left+1
如果nums[i]+nums[left]+nums[right]=target，则返回target
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        v  = 999999
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n -1 
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    return target
                elif nums[i] + nums[left] + nums[right] > target:
                    '''
                    如果nums=[-1,1,2],target=1，此时-1+1+2>target，在跳出循环前，需要先判断-1+1+2是否是最优解
                    '''
                    if abs(nums[i] + nums[left] + nums[right] - target ) < v:
                        v = abs(nums[i] + nums[left] + nums[right] - target )
                        ans = nums[i] + nums[left] + nums[right]
                    right = right - 1
                else:
                    if abs(nums[i] + nums[left] + nums[right] - target ) < v:
                        v = abs(nums[i] + nums[left] + nums[right] - target )
                        ans = nums[i] + nums[left] + nums[right]
                    left = left + 1
                                        
                if left < right and abs(nums[i] + nums[left] + nums[right] - target ) < v:
                    v = abs(nums[i] + nums[left] + nums[right] - target )
                    ans = nums[i] + nums[left] + nums[right]

        return ans
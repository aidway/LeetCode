class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        算法：枚举每个数字，用maps变量（字典类型）记录每个数字需要哪个数字可以完成匹配
        '''
        
        '''
        maps[key] = value
        key:被需要的数字
        value:被谁需要的数字的index
        例子：
        maps[2] = 1
        数字2被nums[1]需要，即 2 + nums[1] = target
        '''
        maps = {}
        ind = 0
        for n1 in nums:
            n2 = target - n1
            
            # 如果n1被需要过
            if n1 in maps.keys() :
                return [maps[n1],ind]
                
            # n2 被 nums[ind]需要
            maps[n2] = ind
            
            ind += 1
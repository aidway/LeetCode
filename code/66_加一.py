'''
Ëã·¨£ºÄ£Äâ
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = [0 for i in range(n+1)]
        digits[n-1] += 1
        ans[1:] = digits
        
        i = n
        while i >=1 and ans[i] > 9:
            ans[i] -= 10
            ans[i-1] += 1
            i -= 1

        return ans if ans[0] > 0 else ans[1:]
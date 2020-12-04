'''
算法：模拟。
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 去两侧空格
        s = s.strip()
        # 分割
        ans = s.split(' ')
        return len(ans[-1])
'''
�㷨��ģ�⡣
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # ȥ����ո�
        s = s.strip()
        # �ָ�
        ans = s.split(' ')
        return len(ans[-1])
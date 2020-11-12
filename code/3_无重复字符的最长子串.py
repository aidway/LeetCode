'''
算法：遍历。
      设置head指向子串的起始位置。
      记录每个字符上一次出现的位置，如果当前的字符曾经出现过，需要将head更新为最近一次该字符出现位置的下一个位置。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        d = {}
        slen = len(s)
        ans = 0
        
        for i in range(slen):
            
            '''
            1. 如果s[i]已经出现过，需要将head更新为s[i]上次出现位置+1
            2. 为何加head < d[s[i]] + 1 ？ 防止 abba
            '''
            if s[i] in d.keys() and head < d[s[i]] + 1:
                head = d[s[i]] + 1

            # 计算当前子串长度
            ans_tmp = i - head + 1

            ans = max(ans_tmp, ans)

            d[s[i]] = i
        return ans
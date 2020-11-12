'''
�㷨����̬�滮������maps[i][j]��ʾs[i:j]�Ƿ�Ϊ�����ַ��������Ϊ����s[i-1]����s[j+1]����ôs[i-1:j+1]ҲΪ�����ַ�����
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        maps = [[0]*slen for i in range(slen)]
        ans = -1
        p = q = 0
        for i in range(slen):
            maps[i][i] = 1
            # ��������ַ�һ��
            if i+1 < slen and s[i] == s[i+1]:
                maps[i][i+1] = 1
                p = i
                q = i + 1
        
        # ö���ַ�������
        for L in range(1,slen-1):
            for i in range(1, slen-L):
                j = i + L
                if s[i-1] == s[j] and maps[i][j-1] == 1:
                    maps[i-1][j] = 1
                    if j - (i-1) > ans:
                        ans = j - (i-1)
                        p = i - 1
                        q = j
        return s[p:q+1]


'''
�㷨��ģ��
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        ans_p = ''
        slen = len(s)
        for i in range(slen):
            if slen - i + 1 <= len(ans_p):
                break
            for j in range(slen,i,-1):
                s_sub = s[i-1:j]
                if s_sub == s_sub[::-1] and len(s_sub) > len(ans_p):
                    ans = len(s_sub)
                    ans_p = s_sub
                    break

        return ans_p
'''
�㷨��������
      ����headָ���Ӵ�����ʼλ�á�
      ��¼ÿ���ַ���һ�γ��ֵ�λ�ã������ǰ���ַ��������ֹ�����Ҫ��head����Ϊ���һ�θ��ַ�����λ�õ���һ��λ�á�
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        d = {}
        slen = len(s)
        ans = 0
        
        for i in range(slen):
            
            '''
            1. ���s[i]�Ѿ����ֹ�����Ҫ��head����Ϊs[i]�ϴγ���λ��+1
            2. Ϊ�μ�head < d[s[i]] + 1 �� ��ֹ abba
            '''
            if s[i] in d.keys() and head < d[s[i]] + 1:
                head = d[s[i]] + 1

            # ���㵱ǰ�Ӵ�����
            ans_tmp = i - head + 1

            ans = max(ans_tmp, ans)

            d[s[i]] = i
        return ans
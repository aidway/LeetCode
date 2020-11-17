'''
�㷨��ö��+˫��ָ�롣
�赥�ʸ���Ϊlen_word��һ�����ʵĳ���Ϊlen_one_word
��s��ö����ʼλ��i��0~len_word:
    ��s[i:]����i��ʼ����ʼ��left=right=i
    �ж� s[i:i+len_one_word] �Ƿ���words�У��������words����left�ƶ���right�������words�У��жϸô���s[left:rihgt]�г��ֵĴ����Ƿ񳬹���words�еĴ���������������ƶ�left�����δ�������ƶ�right��
'''
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        len_s = len(s)
        len_word = len(words)
        if len_word == 0:
            return []

        len_one_word = len(words[0])
        words_cnt = Counter(words)

        ans = []
        # ��ʼ���ö�٣�����ɸ��������
        for i in range(len_one_word):
            left = right = i
            # ��¼�������Ӵ��г��ֵĴ���
            cnts = {}
            while right < len_s:
                next_word = s[right:right+len_one_word]
                # ����words��
                if next_word not in words :
                    left = right = right + len_one_word
                    cnts = {}
                else:
                    # ���µ������Ӵ��ĳ��ִ���������δ�ж�next_word�Ƿ�Ӧ�ü���cnts�ͽ������~�����Ϊʲô����Ҫ��1��ԭ��
                    if next_word not in cnts.keys():
                        cnts[next_word] = 1
                    else:
                        cnts[next_word] = cnts[next_word] + 1
                        
                    # ���ִ������
                    if cnts[next_word] > words_cnt[next_word]:
                        cnts[next_word] = cnts[next_word] - 1
                        cnts[s[left:left+len_one_word]] = cnts[s[left:left+len_one_word]] - 1
                        left = left + len_one_word
                    else:
                        right = right + len_one_word
                        
                # ƥ��ɹ�
                if right - left == len_word * len_one_word:
                    ans.append(left)
                    cnts[s[left:left+len_one_word]] = cnts[s[left:left+len_one_word]] - 1
                    left = left + len_one_word
        
        return list(set(ans))
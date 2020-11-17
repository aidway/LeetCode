'''
算法：枚举+双向指针。
设单词个数为len_word，一个单词的长度为len_one_word
对s，枚举起始位置i：0~len_word:
    对s[i:]，从i开始，初始化left=right=i
    判断 s[i:i+len_one_word] 是否在words中，如果不在words，将left移动到right；如果在words中，判断该词在s[left:rihgt]中出现的次数是否超过在words中的次数，如果超过，移动left，如果未超过，移动right。
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
        # 起始点的枚举，类似筛法求素数
        for i in range(len_one_word):
            left = right = i
            # 记录单词在子串中出现的次数
            cnts = {}
            while right < len_s:
                next_word = s[right:right+len_one_word]
                # 不在words中
                if next_word not in words :
                    left = right = right + len_one_word
                    cnts = {}
                else:
                    # 更新单词在子串的出现次数。（还未判断next_word是否应该加入cnts就将其加入~这就是为什么后续要减1的原因）
                    if next_word not in cnts.keys():
                        cnts[next_word] = 1
                    else:
                        cnts[next_word] = cnts[next_word] + 1
                        
                    # 出现次数溢出
                    if cnts[next_word] > words_cnt[next_word]:
                        cnts[next_word] = cnts[next_word] - 1
                        cnts[s[left:left+len_one_word]] = cnts[s[left:left+len_one_word]] - 1
                        left = left + len_one_word
                    else:
                        right = right + len_one_word
                        
                # 匹配成功
                if right - left == len_word * len_one_word:
                    ans.append(left)
                    cnts[s[left:left+len_one_word]] = cnts[s[left:left+len_one_word]] - 1
                    left = left + len_one_word
        
        return list(set(ans))
'''
算法：递归。对s，从0开始枚举每个起始位置，根据接下来的子串是否为words中的单词判断是否继续递归处理。
'''
class Solution:
    def run(self, s, words):
        nw = len(words)
        if len(words) ==0:
            return True
        flag = []
        '''
        枚举words中的单词，如果能匹配上，则继续枚举
        '''
        for i in range(nw) :
            if words[i] not in flag:
                flag.append(words[i])
            else:
                continue
            n = len(words[i])
            # 匹配成功
            if s[:n] == words[i]:
                res = self.run(s[n:], words[:i]+words[i+1:])
                if res is True:
                    return True

        return False

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ns = len(s)
        nw = len(set(words))
        ans = []
        d = []

        total_words_len = 0
        for i in words:
            total_words_len = total_words_len + len(i)

        i = 0
        '''
        从位置i开始，枚举words中的每个单词，如果能匹配上，进入递归
        '''
        while i < ns - total_words_len + 1:
            # 如果s[i:i+total_words_len]已经遍历过，则只需要根据之前的结果就能判断，无需继续递归
            if i >=total_words_len and  s[i:i+total_words_len] in s[:i] :
                if s[i:i+total_words_len] in d:
                    ans.append(i)
                i = i + 1
                continue

            flag = []
            for j in range(nw):
                if words[j] in flag:
                    continue
                else:
                    flag.append(words[j])

                n = len(words[j])
                if i+n <= ns and s[i:i+n] == words[j]:
                    res = self.run(s[i+n:], words[0:j] + words[j+1:])
                    if res == True:
                        d.append(s[i:i+total_words_len])
                        ans.append(i)
            i = i + 1
        return list(set(ans))
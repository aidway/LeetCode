'''
�㷨���ݹ顣��s����0��ʼö��ÿ����ʼλ�ã����ݽ��������Ӵ��Ƿ�Ϊwords�еĵ����ж��Ƿ�����ݹ鴦��
'''
class Solution:
    def run(self, s, words):
        nw = len(words)
        if len(words) ==0:
            return True
        flag = []
        '''
        ö��words�еĵ��ʣ������ƥ���ϣ������ö��
        '''
        for i in range(nw) :
            if words[i] not in flag:
                flag.append(words[i])
            else:
                continue
            n = len(words[i])
            # ƥ��ɹ�
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
        ��λ��i��ʼ��ö��words�е�ÿ�����ʣ������ƥ���ϣ�����ݹ�
        '''
        while i < ns - total_words_len + 1:
            # ���s[i:i+total_words_len]�Ѿ�����������ֻ��Ҫ����֮ǰ�Ľ�������жϣ���������ݹ�
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
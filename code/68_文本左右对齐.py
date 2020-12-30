'''
算法：贪心。
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        
        # 贪心：每行尽量多放单词
        res = []
        i = 0
        ls = []  # 每行单词个数
        while i < n:
            ans = [words[i]]
            wn = len(words[i])
            j = i + 1
            while j < n:
                if wn + len(words[j]) + 1 <= maxWidth:
                    ans.append(words[j])
                    wn += len(words[j]) + 1
                else:
                    break
                j += 1
            i += j - i
            res.append(ans)
            ls.append(wn)

        # 分配单词间的空格
        # 如果不是最后一行，每个单词先均分，多余的靠前放
        # 如果是最后一行，每个单词间一个空格，最后一个单词后补足空格
        result = []
        for i in range(len(res)):
            words_num = len(res[i])
            space_num = maxWidth - (ls[i] - words_num + 1)
            tmps = res[i][0]
            if words_num == 1:
                result.append(tmps + ' '*(maxWidth-len(tmps)))
                continue

            k1 = space_num // (words_num-1)
            k2 = space_num % (words_num-1)

            for j in range(1,words_num):
                total = k1
                if i == len(res)-1:
                    # 如果是最后一行，每个单词间一个空格
                    total = 1
                elif j <= k2:
                    total += 1
                tmps += ' ' * total + res[i][j]

            tmps += ' ' * (maxWidth - len(tmps))
            result.append(tmps)
        return result


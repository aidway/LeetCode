'''
�㷨���ݹ�
'''

class Solution:
    def deal(self, d,ans, digit):
        v = []
        for i in d[digit]:
            for j in ans:
                v.append(j+i)
        return v

    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],
        "6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}

        ans = []
        if len(digits) == 0:
            return ans

        # ���ȴ����һ���ַ�
        ans.extend(d[digits[0]])
        # ���εݹ鴦�������ַ�
        for i in digits[1::]:
            ans = self.deal(d, ans, i)
        return ans
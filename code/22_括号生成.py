'''
�㷨������
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        ans = {}
        ans[1] = ['()']
        v = set()
        # ��������
        for i in range(1, n):
            j = ans[i]
            v = set()
            # ������ͬ���Ÿ���
            for k in range(len(j)):
                for p in range(len(j[k])):
                    v.add(j[k][0:p+1]+'()'+j[k][p+1:])
            ans[i+1] = list(v)
        return list(v)
'''
�㷨��ջ
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        v = []     # ��Ϊջ�����ַ�
        ind = []   # ��ջ���ַ���Ӧ����¼�ַ�λ��
        flag = [0 for i in range(n)]  # flag[i]=1 ��iλ�õ��ַ�����������
        
        for i in range(n):
            nv = len(v)
            if nv > 0 and  s[i] == ')' and  v[-1] == '(':
                flag[ind[-1]] = 1
                flag[i] = 1
                ind.pop()
                v.pop()
            else:
                v.append(s[i])
                ind.append(i)
                
        # ͳ��������ţ����1��
        tmp = 0
        best = 0
        for i in flag:
            if i == 1:
                tmp = tmp + 1
            
            if tmp > best:
                best = tmp

            if i == 0:
                tmp = 0
            

        return best
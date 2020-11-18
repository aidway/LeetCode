'''
算法：栈
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        v = []     # 作为栈，存字符
        ind = []   # 与栈中字符对应，记录字符位置
        flag = [0 for i in range(n)]  # flag[i]=1 第i位置的字符是正常括号
        
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
                
        # 统计最长的括号（最长的1）
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
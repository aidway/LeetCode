'''
算法：无聊算法
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        digit_except_zero = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
        e = ['e']
        flag = ['+', '-']
        decimal  = ['.']

        right = digit + e + flag + decimal

        # 去除空格
        s = s.strip()
        
        if len(s) == 0:
            return False
            
        if s[0] in flag:
            s = s[1:]

        n = len(s)
        if n == 0:
            return False
        if n == 1 and s[0] not in digit:
            return False

        e_num = 0
        flag_num = 0
        flag_p = 0
        decimal_num = 0
        for i in range(n):
            if s[i] not in right:
                return False
            elif s[i] == 'e':
                e_num += 1
                if e_num > 1:
                    return False
            elif s[i] in flag:
                flag_num += 1
                flag_p = i
                if flag_num > 1:
                    return False
                if i > 0 and s[i-1] != 'e':
                    return False
            elif s[i] == '.':
                decimal_num += 1
                if decimal_num > 1:
                    return False
                
        if s[0] in flag:
            s = s[1:]

        if s == '.':
            return False

        if e_num == 1:
            s1 = s.split('e')[0]
            s2 = s.split('e')[1]

            n1 = len(s1)
            n2 = len(s2)
            if n1 == 0 or n2 == 0:
                return False
            
            if '.' in s2:
                return False
            
            if s1 == '.':
                return False
            if s2 == '+' or s2 == '-' or s2 == '.':
                return False
        else:
            if flag_p > 0:
                return False

        return  True 
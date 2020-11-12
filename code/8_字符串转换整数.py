'''
�㷨��ģ�⣬��ˢ
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = pow(2,31) - 1
        INT_MIN = pow(2, 31) * (-1)

        # 1. ȥ�ո�
        s = s.strip()

        # 2. Ϊ��
        if s == "":
            return 0

        # 3. �жϷ���
        flag = 1
        if s[0] == '-':
            s = s[1:]
            flag = -1
        elif s[0] == '+':
            flag = 1
            s = s[1:]

        # 4. �ж�Ϊ��
        if s == "":
            return 0
        
        # 5. �ж������Ƿ�Ϊ����
        if not s[0].isdecimal():
            return 0
        
        
        # 6. ת��
        slen = len(s)
        ans = ""
        for i in range(slen):
            if not s[i].isdecimal():
                break
            ans = ans + s[i]

        # 7. ����
        ans_int = int(ans) * flag
        if ans_int > INT_MAX:
            return INT_MAX
        elif ans_int < INT_MIN:
            return INT_MIN
        else:
            return ans_int
'''
�㷨����̬�滮
'''
class Solution:
    def matches(self, s, p ):
        if p == '.':
            return True
        else:
            return s == p

    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        '''
        f : (m+1) * (n+1) ����
        f[i][j] : s[:i]�ܱ�p[:j] ƥ��
        s = abc
        p = aaa
        f[1][1] = True
        ԭ��s[:1]=a p[:1]=a �ܹ�ƥ��

        s=aa
        p=a*
        f[0][2] = True
        ԭ��s[:0] = '' p[:2]=a* �ܹ�ƥ��
        '''
        f = [[False] * (n+1)  for _ in range((m+1))]
        # ���ܱ���ƥ��
        f[0][0] = True
        
        '''
        k > 0
        f[0][k] ����ΪTrue������iҪ��0��ʼö��
        f[k][0] һ��ΪFalse���ǿյ��ַ������ܱ��յ�����ƥ�䣬��j��1��ʼƥ��
        '''
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] != '*':
                    if i > 0 and self.matches(s[i-1], p[j-1]):
                        f[i][j] = f[i-1][j-1]
                else:
                    if i > 0 and self.matches(s[i-1], p[j-2]):
                        f[i][j] = f[i-1][j] | f[i][j-2]
                    else:
                        f[i][j] =  f[i][j-2]
                
        return f[m][n]
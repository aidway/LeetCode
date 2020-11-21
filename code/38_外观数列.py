'''
Ëã·¨£ºÄ£Äâ
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        if n == 1:
            return s
        for i in range(2, n+1):
            lens = len(s)
            t = ""
            j = 0
            while j < lens:
                a = 1
                b = s[j]
                while j+1 < lens and s[j] == s[j+1]:
                    a += 1
                    j += 1
                j += 1
                t += str(a) + b
            print(i,t)        
            s = t
        return s
'''
Ëã·¨£º¶ÓÁÐ
'''
class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                ans.append(i)
            n = len(ans)
            if i == ')':
                if n == 0:
                    return False
                elif ans[n-1] != '(':
                    return False
                else :
                    ans.pop()
            if i == ']':
                if n == 0:
                    return False
                elif ans[n-1] != '[':
                    return False
                else :
                    ans.pop()
            if i == '}':
                if n == 0:
                    return False
                elif ans[n-1] != '{':
                    return False
                else :
                    ans.pop()

         
        return len(ans) == 0
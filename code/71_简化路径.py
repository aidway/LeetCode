'''
算法：栈
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        ans = []
        for i in s:
            if i != '' and i != '.':
                if i != '..':
                    ans.append(i)
                elif len(ans) > 0:
                    ans.pop()
              
        res = '/'
        for i in ans:
            res +=  i + '/'

        return res[:-1] if res != '/' else res
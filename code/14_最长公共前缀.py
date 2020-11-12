class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        size = [len(i) for i in strs]
        
        for i in range( min(size), -1, -1 ):
            sub = strs[0][0:i]
            ok = True
            for j in strs:
                if sub != j[0:i]:
                    ok = False
                    break
            if ok:
                return sub
        return ""
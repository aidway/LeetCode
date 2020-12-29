'''
算法：位运算
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x = answer
            y = carry
        
        return bin(x)[2:]


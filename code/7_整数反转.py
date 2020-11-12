class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x >= 0 else -1
        
        x = abs(x)
        n = 0
        while(x != 0):
            a = x % 10
            n = n * 10 + a
            x = x // 10

        n = n * flag
        if n < -2147483648 or n > 2147483647:
            n = 0     
        return n
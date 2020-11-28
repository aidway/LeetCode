'''
算法：模拟
'''
class Solution:
    def multiply(self , num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)

        ans = ["0" for i in range(n1 + n2 + 10)]

        if num1 == "0" or num2 == "0":
            return "0"
 

        num1 = num1[::-1]
        num2 = num2[::-1]

        a, b, c, d = 0, 0, 0, 0
        for i in range(n2):
            a = int(num2[i])
            for j in range(n1):
                b = int(num1[j])
                # 进位
                c = a * b // 10  
                # 当前位
                d = a * b % 10
                # 当前位与之前对应的位置相加
                e = int(ans[i + j]) + d
                # 当前位相加后产生的进位
                c += e // 10
                # 最终的当前位
                e = e % 10
                ans[i + j] = str(e)
                ans[i + j + 1] = str(int(ans[i + j + 1]) + c)
                k = i + j + 1
                while int(ans[k]) > 10:
                    t = int(ans[k]) // 10
                    ans[k] = str(int(ans[k]) % 10)
                    ans[k + 1] = str(int(ans[k + 1]) + t)
                    k += 1
                    
                    
        v = ""
        ok = False
        for i in ans[::-1]:
            if i != "0":
                ok = True
            if ok:
                v += i


        return v

 
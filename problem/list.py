a=[]
b=[]
b=[1]
# 加入的其实是b的引用
a.append(b)
print(a)
b.pop()
print(a)
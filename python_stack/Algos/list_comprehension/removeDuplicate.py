nums=[1,2,3,3,4,4,5,6,6,7,8]
b=[]
[b.append(n) for n in nums if n not in b]
print(b)



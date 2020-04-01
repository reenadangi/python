def compareTriplets(a, b):
    arr=[]
    acount=0
    bcount=0  
    for i in range(len(a)):
        if a[i]>b[i]:
            acount+=1
        elif b[i]>a[i]:
            bcount+=1
    arr.append(acount)
    arr.append(bcount)
    return arr   
a=[2,3,5]
b=[1,3,6]
print(compareTriplets(a,b))

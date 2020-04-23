def merge(num1,m,num2,n):
    m=m-1
    n=n-1
    index=len(num1)-1
    while index>=0:
        if m<0:
            num1[index]=num2[n]
            n-=1
        elif n<0:
            num1[index]=num1[m]
            m-=1
        else:
            if num1[m]>num2[n]:
                num1[index]=num1[m]
                m-=1
            else:
                num1[index]=num2[n]
                n-=1
        index-=1
    return num1

     
print(merge([1,2,3,0,0,0],3,[2,5,6],3))
print(merge([0],0,[1],1))
print(merge([1,0],1,[2],1))


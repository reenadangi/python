def reverseString(str):
    s=list(str)
    start=0
    end=len(str)-1
    while(end>start):
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    return "".join(s)
print(reverseString("hello"))
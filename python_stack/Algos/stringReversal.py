def reverseString(str):
    string=list(str)
    start=0
    end=len(string)-1
    while start<end:
        string[start],string[end]=string[end],string[start]
        start+=1
        end-=1
    return ''.join(string)
    
print(reverseString("Hello"))
print("hello world"[::-1])

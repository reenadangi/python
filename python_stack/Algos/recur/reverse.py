def reverseRec(s,start,end):
    if start<=end:
        s[start],s[end]=s[end],s[start]
        return reverseRec(s,start+1,end-1)
    else:
        return s
def reverse(s):
    return reverseRec(s,0,len(s)-1)
    
print(reverse(["h","l","l","o","a"]))
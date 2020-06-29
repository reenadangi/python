def validPalindrome(str):
    s=list(str)
    if len(s)>0:
        start=0
        end=len(s)-1
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
print(validPalindrome("abccba"))

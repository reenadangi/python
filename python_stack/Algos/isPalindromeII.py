def validPalindrome(s):
        start=0
        end=len(s)-1
        del_count=0
        valid=False
        while start<end:
            if s[start]!=s[end]:
                if del_count>0:
                    return False
                else:
                    del_count+=1
                    start+=1
                    end-=1
                    valid=False
            else:
                valid=True
                start+=1
                end-=1
        return valid
print(validPalindrome("cabc"))
      
        
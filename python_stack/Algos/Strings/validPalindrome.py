import re
def validPlindrome(s):
    if len(s)>0:
         s = re.sub(r'\W+', '', s)
         start=0
         end=len(s)-1
         while start<end:
             if s[start]!=s[end]:
                 return False
             start+=1
             end-=1
    return True   
print(validPlindrome('ab ba '))
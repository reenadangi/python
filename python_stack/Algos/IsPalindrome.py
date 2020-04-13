# Palindrome
import re
str="A man, a plan, a canal: Panama"

# def isPalindrome(str):

#     str = re.sub(r'\W+', '', str)
#     end=len(str)-1
#     start=0
#     print(str)
#     while start<end:
#         if str[start].upper()!=str[end].upper():
#             return False
#         start+=1
#         end-=1
#     return True

def isPalindrome(s):
    s = re.sub(r'\W+', '', s)
    start=0
    end=len(s)-1
    while start<end:
        if s[start].upper()!=s[end].upper():
           return False
        else:
            start+=1
            end-=1
    return True

print(isPalindrome(str))
# print(dir(str))
# print(help(str.lower))


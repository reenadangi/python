def repeatedSubstringPattern( str):

    
    if not str:
        return False
        
    ss = (str + str)[1:-1]
    
    if ss.find(str):
        return True
    else:
        return False
print(repeatedSubstringPattern("abab"))
def first_unique_char(s):
    
    for i in range(len(s)):
        if s[i] not in s[i+1:len(s)]:
            if s[i] not in s[:i]:
                return i
      
        
        
print(first_unique_char('leetcode'))

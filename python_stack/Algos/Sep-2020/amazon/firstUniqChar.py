def firstUniqChar(s):
    for i in range(len(s)):
        if(s[i] not in s[i+1:] and s[i] not in s[:i]):
            return s[i]
    return -1
print(firstUniqChar("mleletcode"))
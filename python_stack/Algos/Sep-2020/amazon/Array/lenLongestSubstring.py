def lengthOfLongestSubstring( s):
#sliding window
    if len(s)==0:
        return 0
    dict={}
    max_len=start=0
    for i in range(len(s)):
        if s[i] in dict and start<=dict[s[i]]:
            start+=dict[s[i]]+1
        else:
            max_len=max(max_len,i-start+1)
        dict[s[i]]=i
    return (max_len)
        
print(lengthOfLongestSubstring("abcabcbb"))
       
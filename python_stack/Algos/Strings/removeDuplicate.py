def removeDuplicate(s):
    # s=list(s)
    # i=0
    # for j in range(i+1,len(s)):
    #     if s[j]!=s[i]:
    #         i+=1
    #         s[i]=s[j]
    # print (i)
    # return ''.join(s[:i+1])
    output=''
    s=list(s)
    for c in s:
        if c not in output:
            output=output+c
    return output


print(removeDuplicate("azabcdefg"))

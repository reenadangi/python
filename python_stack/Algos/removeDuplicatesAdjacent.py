# Input: "abbaca"
# Output: "ca"
def removeAdjacentDuplicate(S):
    res = []
    for i in range(len(S)):
        if len(res) > 0 and S[i] == res[-1]:
            res.pop()
        else:
            res.append(S[i])
    
    return ''.join(res)
# print(removeAdjacentDuplicate(["a","b","b","a","c","a"]))
print(removeAdjacentDuplicate(["a","a","b","a","b","a","a","b"]))

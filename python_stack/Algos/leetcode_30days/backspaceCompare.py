# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

def backspaceCompare(S,T):
    q=[]
    p=[]
    for i in range(0,len(S)):
        if S[i]!='#':
            q.append(S[i])
        elif len(q)>0:
            q.pop()
    for i in range(0,len(T)):
        if T[i]!='#':
            p.append(T[i])
        elif len(p)>0:
            p.pop()
    return p==q
    
# S = "ab#c", T = "ad#c"
print(backspaceCompare("ab#c","ad#c"))
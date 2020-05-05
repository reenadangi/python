def removeOuterParentheses(S):
    res=[]
    balance=0
    k=0
    for i in range(len(S)):
        if S[i]=='(':
            balance+=1
        elif S[i]==')':
            balance-=1
        if balance==0:
            res.append(S[k+1:i])
            k=i+1
    
    return "".join(res)

print(removeOuterParentheses("(()())(())"))




def parenValid(str):
    counter=0
    for c in str:
        if c=='(':
            counter+=1
        if c==')':
            counter-=1
        if counter<0:
            return False
    if counter!=0:
        return False
    else: return True
print(parenValid('(()))'))
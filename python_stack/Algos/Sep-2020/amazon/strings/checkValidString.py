def checkValidString(self, s):
    if(len(s)<1):
        return True
    balance=0
    for c in s:
        if c==')':
            balance-=1
        else:
            balance+=1
        if balance<0:
            return False
    if balance==0:
        return True
    balance=0
    for c in reversed(s):
        if c=='(':
            balance-=1
        else:
            balance+=1
        if balance<0:
            return False
    return True

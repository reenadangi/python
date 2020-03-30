# Split a String in Balanced Strings

def balanceStrings(s):
    balance=0
    count=0
    for i in range (len(s)):
        print (s[i])
        if s[i]=='R':
            balance+=1
        else:
            balance-=1
        if balance==0:
            count+=1
    return count

print(balanceStrings("RLRRLLRLRL"))
# solve this problem with stack
def removeKdigits(num,k):
    stack=[]
    for element in num:
        while k>0 and stack and stack[-1]>element:
            stack.pop()
            k=k-1
        stack.append(element)
    if k!=0:
        stack.pop()
        k-=1
    # convert it back to string, if any preceding 0 strip them and return "0" if only "0" is left
    return "".join(stack).lstrip("0") or "0"

print(removeKdigits("1432219",3))

       








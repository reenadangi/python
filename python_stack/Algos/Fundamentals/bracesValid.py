# it are valid. For example, given the input string
# "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!" , return
# true . Given "d(i{a}l[t]o)n{e" , return
# false . Given "a(1)s[O(n]0{t)0}k" , return
# false .
def bracesValid(str):
    myStack=[]
    mapping={"(":")","{":"}","[":"]"}
    for p in str:
        if p in('(','{','['):
            myStack.append(p)
        if p in (')','}',']'):
            if myStack:
                topElement=myStack.pop()
                topElement=mapping[topElement]
                if topElement!=p:
                    return False
            else:
                return False
    if myStack: 
        return False
    else: 
        return True

print(bracesValid("w(a{t}s[o(n{c}o)m]e)h[e{r}e]!"))


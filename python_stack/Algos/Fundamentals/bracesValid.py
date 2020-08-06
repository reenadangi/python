# it are valid. For example, given the input string
# "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!" , return
# true . Given "d(i{a}l[t]o)n{e" , return
# false . Given "a(1)s[O(n]0{t)0}k" , return
# false .
def bracesValid(str):
    mapping={"(":")","{":"}","[":"]"}
    myStack=[]
    for c in str:
        if c in ('(','{','['):
            myStack.append(c)
        elif c in (')','}',']'):
            if myStack:
                top=myStack.pop()
                if c!=mapping[top]:
                    return False
            else:
                return False    
    if myStack: return False
    else: return True

print(bracesValid("w(a{t}s[o(n{c}o)m]e)h[e{r}e]!"))             
        



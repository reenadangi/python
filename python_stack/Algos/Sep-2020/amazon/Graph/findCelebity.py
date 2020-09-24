MATRIX ={
    0:[1,2],
    1:[],
    2:[1,3],
    3:[1,0]
}
  
def knows(a, b):
    if b in MATRIX[a]:
        return True
    return False
    # there could be only one celebrity 
def findCelebity(n):
    candidate=0
#    check who is the candidate for celebrity
    for i in range(1,n):
        if knows(candidate,i):
            # if candidate knows i then candidate is not celeb, i becomes candidate
            candidate = i
    print(candidate)
    for i in range(n):
        if(i != candidate and (knows(candidate,i) or  not knows(i,candidate))):
            return -1
    return candidate

print(findCelebity(4))
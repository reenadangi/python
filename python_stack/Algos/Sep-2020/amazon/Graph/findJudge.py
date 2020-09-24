def findJudge(N,trust):
    trust_count=[0]*N
    for t in trust:
        trust_count[t[0]-1] -=1
        trust_count[t[1]-1] +=1
    print(trust_count)
    for i in range(N):
        if trust_count[i]==N-1:
            return i+1
    return -1

print(findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(findJudge(2,[[1,2]]))
print(findJudge(3,[[1,2],[2,3]]))
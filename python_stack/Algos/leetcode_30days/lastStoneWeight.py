# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
def lastStoneWeight(stones):
    
    while(len(stones)>1):
        stones=sorted(stones)
        print(stones)
        large=stones.pop()
        small=stones.pop()
        stones.append(large-small)

    return stones[0]

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1,3]))


def pushFront(nums,k):
    nums.insert(0,k)
    return nums

print(pushFront([1,2,3,4,5,6],0))

def insertAt(nums,k,value):
    nums.insert(k,value)
    return nums
print(insertAt([1,2,3,4,5,6],0,78))


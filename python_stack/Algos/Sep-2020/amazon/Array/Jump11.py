# Given an array of non-negative integers, 
# you are initially positioned at the first index of the array.
# Each element in the array represents 
# your maximum jump length at that position.

# Determine if you are able to reach the last index.
# start from the last 
def canJump(nums):
    lastIndex=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if (i + nums[i] >= lastIndex):
            lastIndex = i
        
    if lastIndex==0:
        return True
    else:
        return False

    
print(canJump([2,3,1,1,4]))
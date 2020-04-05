# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
def moveZero(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
           nums[j]=nums[i]
           j+=1
    for i in range(j,len(nums)):
        nums[i]=0
    return nums

print (moveZero([0,1,0,3,12]))
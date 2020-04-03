# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
def findMaxIndex(nums):
    maxIndex=0
    for i in range(1,len(nums)):
        if nums[maxIndex] < nums[i]:
            maxIndex=i
    return maxIndex 

def maxCrossingSum(nums, l, m, h) : 
    # Include elements on left of mid. 
    sm = 0; left_sum = -10000
    for i in range(m, l-1, -1) : 
        sm = sm + nums[i] 
        if (sm > left_sum) : 
            left_sum = sm 
    # Include elements on right of mid 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + nums[i] 
        if (sm > right_sum) : 
            right_sum = sm 
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum; 

def max_subArray_divide(nums,lowest,highest):
    if lowest==highest:
        return nums[lowest]
    # Find Middle point
    mid=(lowest+highest)//2
    print(mid) 
    left_sum=  max_subArray_divide(nums,lowest,mid)
    right_sum= max_subArray_divide(nums,mid+1,highest)
    cross_sum=maxCrossingSum(nums, lowest, mid, highest)
    print(left_sum,right_sum,cross_sum)
    return max(left_sum,right_sum,cross_sum)
   

def max_subArray(nums):
    # divide and conqure
   return max_subArray_divide(nums,0,len(nums)-1)


print(max_subArray([-2,1,-3,4,-1,2,1,-5,4]))
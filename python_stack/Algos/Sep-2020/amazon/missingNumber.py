# Given an array containing n distinct numbers taken from
#  0, 1, 2, ..., n, find the one that is missing from the array.

# input: [3,0,1]
# Output: 2
def missingNumber(nums):
        sumIfNoneMissing = len(nums)
        actualSum = 0
        for i in range(len(nums)):
            sumIfNoneMissing += i
            actualSum += nums[i]
        return sumIfNoneMissing - actualSum
print(missingNumber([3,0,1]))
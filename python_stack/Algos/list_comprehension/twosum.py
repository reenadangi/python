# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
nums=[2,7,11,15]
target=9
nums=[(n,m) for n,m in nums if n+m==target]
print(nums)
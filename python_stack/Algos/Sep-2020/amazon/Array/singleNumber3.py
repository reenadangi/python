# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
def singleNumber(nums):
    nums_set=set()
    for n in nums:
        if n in nums_set:
            nums_set.remove(n)
        else:
            nums_set.add(n)
    return(nums_set)
print(singleNumber([1,2,1,3,2,5]))
    
 
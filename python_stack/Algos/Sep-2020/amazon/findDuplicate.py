# Input: nums = [3,1,3,4,2]
# Output: 3
def findDuplicate(nums):
    new_set=set()
    for n in nums:
        if n in new_set:
            return n
        else:
            new_set.add(n)
    return -1
print(findDuplicate([1,2,3,4,1]))

def containduplicate(nums):
    d=[]
    for i in nums:
        if i in d:
            return True
        d.append(i)
    return False
print(containduplicate([2,3,4,5,6]))

# another way is to sort
def sort(nums):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums
def removeDuplicates(nums):
    nums=sort(nums)
    slow=0
    fast=1
    while fast<=len(nums):
        if nums[slow]==nums[fast]:
            fast+=1
        else:
            slow+=1
            fast+=1
    while slow<=len(nums):
        nums.pop()
        slow+=1
    return nums
print(removeDuplicates([3,4,5,6,3,7,9]))
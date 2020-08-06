def containduplicate(nums):
    lst=[]
    for i in nums:
        if i in lst:
            return True
        lst.append(i)
    return False
print(containduplicate([1,2,7,3,4]))

# sort - in place
def sort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums

def removeDuplicates(nums):
    i=0
    for j in range(i+1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return nums[:i]
    
    
print(removeDuplicates([3,4,5,6,3,7,9]))
nums=sort([55,5,6,6,33,1,0])
print(removeDuplicates(nums))


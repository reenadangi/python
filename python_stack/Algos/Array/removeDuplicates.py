# remove duplicates from a sorted array
def removeDuplicates(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            # it's not duplicate
            i+=1
            nums[i]=nums[j]
            
    return nums[:i+1]

    
print(removeDuplicates([1,1,2]))
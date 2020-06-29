def sort(nums):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums
print(sort([3,4,6,6,2,8,19,59,0]))
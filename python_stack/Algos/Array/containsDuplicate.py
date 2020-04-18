def containsDuplicate(nums):
    # for i in range(len(nums)):
    #     if nums[i] in nums[i+1:]:
    #         return True
    # return False

    #sort and look 
    # nums=sorted(nums)
    # for i in range(len(nums)-1):
    #     if nums[i]==nums[i+1]:
    #         return True
    # return False

    d=[]
    for i in nums:
        if i in d:
            return True
        d.append(i)
    return False

print(containsDuplicate([1,2,1,3,4]))
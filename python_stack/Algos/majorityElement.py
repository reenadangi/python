def majorityElement(nums):
    lst={}
    for i in nums:
        if i not in lst:
            lst[i]=1
        if lst[i] > len(nums)//2:
            return i
        else:
            lst[i]=lst[i]+1
            
    # print(lst)
    # print(max(lst))
print(majorityElement([3,3,4]))

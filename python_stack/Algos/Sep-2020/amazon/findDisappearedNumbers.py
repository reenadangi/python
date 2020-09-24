def findDisappearedNumbers(nums):
    s=set()
    count=1
    for i in nums:
        if count not in nums:
            s.add(count)
    return s
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        



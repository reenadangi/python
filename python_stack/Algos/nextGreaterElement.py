def nextGreaterElement(nums1, nums2):
    res=[]
    for i in nums1:
        for j in nums2[nums2.index(i):]:
            if j>i:
                res.append(j)
                break
        else:
            res.append(-1)
    return res    

print(nextGreaterElement([4,1,2],[1,3,4,2]))
# num1 is subset of num2

def mergeSortedArray(nums1, m, nums2, n):
    i=j=0
    # nums1=nums1[:m]+nums2
    # return sorted(nums1)
    while j<n and i<m:
        if nums2[j]<=nums1[i]:
            # insert in num1
            nums1.insert(i+1,nums2[j])
            j+=1
            i+=1
        i+=1
    while j<m:
        nums1.insert(i+1,nums2[j])
        j+=1
        i+=1
        
    del nums1[n+m:]
    return nums1
print(mergeSortedArray([1,2,3,0,0,0],3,[2,5,6],3))


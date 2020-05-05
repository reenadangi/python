def decompressRLElist(nums):
    arr=[]
    i=0
    while(i<len(nums)-1):
        j=nums[i]
        while(j>0):
            arr.append(nums[i+1])
            j-=1
        i+=2
    print(arr)
decompressRLElist([1,1,2,3])


        
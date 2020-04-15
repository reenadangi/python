def findMaxConsecutiveOnes(nums):
    arr=[]
    count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        elif nums[i]==0:
            arr.append(count)
            count=0
        if count:
            arr.append(count)
    return max(arr)
  
print(findMaxConsecutiveOnes([1,1,1,1,1,0]))
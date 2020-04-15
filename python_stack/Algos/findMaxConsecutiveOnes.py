def findMaxConsecutiveOnes(nums):
    max=currentMax=0
    for i in range(len(nums)):
        if nums[i]==1:
            currentMax+=1
        elif nums[i]==0:
            currentMax=0
        if currentMax>max:
           max=currentMax
    return max
  
print(findMaxConsecutiveOnes([1,1,1,1,1,0]))
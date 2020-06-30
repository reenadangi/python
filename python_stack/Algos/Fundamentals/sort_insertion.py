def sort(nums):
    for i in range(len(nums)):
        j=i-1
        current=nums[i]
        while j>=0 and current<nums[j]:
            nums[j+1],nums[j]=nums[j],nums[j+1] #Shift value
            j-=1
        
    print(nums)
sort([2,3,4,1,5,1,6,7,0])        
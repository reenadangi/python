# Another Example:
# 12, 11, 13, 5, 6
nums=[ 2,3,4,1,5,1,6,7,0]
def sort(nums):
    for i in range(1,len(nums)):
        current=nums[i]
        j=i-1
        while j>=0:
            if current<nums[j]:
                nums[j+1],nums[j]=nums[j],nums[j+1] #Shift value
            else:
                break
            j-=1
    return nums

sort(nums)
print(nums)
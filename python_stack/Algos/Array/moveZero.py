# def moveZeroes(nums):
#     j=0
#     for i in range(0,len(nums)):
#         if nums[i]!=0:
#             nums[j]=nums[i]
#             j+=1
#     while j<=i:
#         nums[j]=0
#         j+=1
#     return nums

# move all zeros to end
def moveZeroes(nums):
    i=0
    j=0
    while j<len(nums):
        if nums[j]!=0:
            nums[i]=nums[j]
            i+=1
            j+=1
        else: j+=1
    while i<len(nums):
        nums[i]=0
        i+=1
    return nums
            
print(moveZeroes([0,1,0,3,12]))
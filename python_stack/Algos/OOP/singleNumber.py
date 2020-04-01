# Given a non-empty array of integers, 
# every element appears twice except for one. Find that single one.
def findSingle(nums): 
    print(set(nums))
    return 2 * sum(set(nums)) - sum(nums)
    # res = nums[0] 
    # n=len(nums)
    # # Do XOR of all elements and return 
    # for i in range(1,n): 
    #     res = res ^ nums[i] 
    # return res 
# Driver code 
ar = [0, 3, 5, 4, 5, 3, 4]
 
print(findSingle(ar)) 

arr=["Apple","Banana","Banana","Orange"]
print(set(arr))
  # for i in range(len(nums)):
        #     found=False
        #     for j in range(len(nums)):
        #         if i!=j and nums[i]==nums[j]:
        #             found=True
        #     if found==False:
        #         return nums[i]

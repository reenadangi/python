# Another Example:
# 12, 11, 13, 5, 6
nums=[ 12, 11, 13, 5, 6]
def sort(nums):
    # start with 2nd position
   for i in range (1,len(nums)):
       key=nums[i]
       j=i-1
       while j>=0 and nums[j]>key:
           nums[j+1]=nums[j]
           j-=1
       nums[j+1]=key  
   print(nums)   
    
sort(nums)
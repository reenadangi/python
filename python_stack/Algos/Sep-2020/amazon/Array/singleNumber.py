# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Input: [2,2,1]
# Output: 1

def singleNumber(nums):
    nums.sort()
    print(nums)
    for i in range(0,len(nums),2):
        if i==len(nums)-1:
            return nums[i]
        elif nums[i]!=nums[i+1]:
            return nums[i]
            
    return -1

def _singleNumber(nums):
    nums_set=set()
    for n in nums:
        if n in nums_set:
            nums_set.remove(n)
        else:
            nums_set.add(n)
    return(nums_set.pop())
      
            
   
       

           
print(_singleNumber([2,4,1,2,1,3,3]))
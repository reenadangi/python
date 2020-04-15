# import math
# def productExceptSelf(nums):
#     arr=[]
#     product=1
#     for i in range(len(nums)):
#         arr.append(math.prod(nums[:i])* math.prod(nums[i+1:]))
#     return arr
# print(productExceptSelf([1,2,3,4]))
#  [24,12,8,6]

def productExceptSelf(nums):
    ans = [1 for _ in nums]
    left = 1
    right = 1
    for i in range(len(nums)):
            ans[i] *= left
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        
    return ans
print(productExceptSelf([2,3,4,5]))

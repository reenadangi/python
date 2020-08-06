def replaceWithZero(nums):
    for i in range(len(nums)):
        if nums[i]<0:
            nums[i]=0
    return nums
print(replaceWithZero([1,2,3,-8,-7]))

def moveForward(nums):
    for i in range(len(nums)-1):
        nums[i]=nums[i+1]
    nums[-1]=0
    return nums
print(moveForward( [1,2,3]))

def reverse(nums):
    start=0
    end=len(nums)-1
    while start<=end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
    return nums
print(reverse([1,2,3,4,5]))
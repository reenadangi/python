def remove(nums,n):
    # arr2=[]
    # for i in range(len(nums)):
    #     if i!=n:
    #         arr2.append(i)
    # return arr2
    nums.remove(n)
    return nums
def removeLast(nums):
    return nums[:-1]

def removeAt(nums,n):
    del nums[n]
    return nums
def removeLastFound(arr,n):
    index=arr[::-1].index(n)
    del arr[(len(arr)-1-index)]
    return arr

# print(removeVals([20,30,40,50,60,70],2,4))
print(remove([2,3,0,4,5,6,7,8,9,0],0))
print(removeLast([2,3,0,4,5,6,7,8,9,0,19]))
print(removeAt([2,3,0,4,5,6,7,8,9,0,19],2))
print("remove last", removeLastFound([2,3,0,4,5,6,7,8,9,0,2,19],2))


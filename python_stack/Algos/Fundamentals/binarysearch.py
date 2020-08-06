# binary search is only possible in sorted array
# Binary search
def search(nums,value):
    for i in nums:
         if i==value:
             return True
    return False
print(search([1,2,3,4,5,6],14))

# Binary search 
# sorted array 
def search_b(nums,value):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==value:
            return mid
        elif nums[mid]>value:
            # value is in left side
            end=mid-1
        else:
            start=mid+1
    return False
print(search_b([1,2,3,45,5],1))

def recBinarySearch(nums,value,start,end):
    if start<=end:
        mid=(start+end)//2
        if nums[mid]==value:
            return mid
        elif nums[mid]>value:
            return recBinarySearch(nums,value,start,mid-1)
        else:
            return recBinarySearch(nums,value,mid+1,end)
    else:
        return False
print(recBinarySearch([1,2,3,4,5,6,7],3,0,6))

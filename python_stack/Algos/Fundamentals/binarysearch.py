# binary search is only possible in sorted array
def search(nums,value):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==value:
            return mid
        if nums[mid]>value:
            # look in only left
            end=mid-1
        else:
            start=mid+1
    return False
print(search([2,3,4,5,6,7,8,9,10],10))

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
print(recBinarySearch([1,2,3,4,5,6,7],8,0,6))

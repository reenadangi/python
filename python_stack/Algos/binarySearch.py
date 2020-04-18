def binarySearch(arr,value):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        # if element is at mid
        if arr[mid]==value:
            return mid
        # else look/left/right
        if arr[mid]<value:
            # value has to be in right
            start=mid+1
        else:
            end=mid-1
    return -1
print(binarySearch([0,2,3,4,5,6,77,88,99],2) )   


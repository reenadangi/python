def binarySearch(arr,start,end,value):
    if start<=end:
        mid=(start+end)//2
        if arr[mid]==value:
            return mid
        elif arr[mid]<value:
            return binarySearch(arr,mid+1,end,value)
        else:
            return binarySearch(arr,start,mid-1,value)
    else: 
        return -1
def search(arr,value):
    return binarySearch(arr,0,len(arr)-1,value)
print(search([1,2,4,5,77,89,100],100))
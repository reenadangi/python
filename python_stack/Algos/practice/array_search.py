# binary search 
# linear search
# recursive binary search
# Binary serch can happen only in sorted array
def binary_search(arr,value):
    # find a mid and look in left and rigth 
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        # if value is in mid
        if arr[mid]==value:
            # found it
            return mid
        elif arr[mid]>value:
            # your value is in left
            end=mid-1
        else:
            # your value is in right
            start=mid+1
    return False

print(binary_search([4,5,6,7,88,99,100],1000))
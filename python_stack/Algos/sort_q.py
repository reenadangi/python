# quick sort
# partition, pivot
def partition(arr,start,end):
    # pivot
    pivot=arr[end]
    pIndex=start
    for i in range(start,end):
        if arr[i]<pivot:
            arr[i],arr[pIndex]=arr[pIndex],arr[i]
            pIndex+=1
    arr[pIndex],arr[end]=arr[end],arr[pIndex]
    return pIndex

def quick_sort(arr,start,end):
    if start<end:
        pIndex=partition(arr,start,end)
        quick_sort(arr,0,pIndex-1)
        quick_sort(arr,pIndex+1,end)
    return arr
def sort(arr):
    return quick_sort(arr,0,len(arr)-1)

print(sort([1,33,2,44,0,-1,88,44,5]))
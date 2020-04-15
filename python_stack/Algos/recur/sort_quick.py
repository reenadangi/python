# Quick Sort
# 1. Partition
# 2. Pivot
# 3. Quicksort

def partition(arr,start,end):
    pivot=arr[end]
    pIndex=start
    for i in range(start,end):
        if arr[i]<pivot:
            arr[i],arr[pIndex]=arr[pIndex],arr[i]
            pIndex+=1
    arr[pIndex],arr[end]=arr[end],arr[pIndex]
    return pIndex
def quickSort(arr,start,end):
    if start<end:
        pIndex=partition(arr,start,end)
        quickSort(arr,start,pIndex-1)
        quickSort(arr,pIndex+1,end)
    return arr
def sort(arr):
    return quickSort(arr,0,len(arr)-1)
print(sort([1,33,4,55,6,9,0,-1]))

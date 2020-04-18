def partition(arr,start,end):
    # Pivot
    pivot=arr[end]
    pIndex=start
    for i in range(start,end-1):
        if arr[i]<pivot:
            arr[i],arr[pIndex]=arr[pIndex],arr[i]
            pIndex+=1
    arr[pIndex],arr[end]=arr[end],arr[pIndex]
    return pIndex

def quick_sort(arr,start,end):
    if start<end:
        pIndex=partition(arr,start,end)
        quick_sort(arr,start,pIndex-1)
        quick_sort(arr,pIndex+1,end)
    return arr

def sort(arr):
   return quick_sort(arr,0,len(arr)-1)
print(sort([11,9,4,22,3,1,4,-1]))
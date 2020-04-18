def partition(arr,start,end):
    # find a pivot
    piviot=arr[end]
    pIndex=start
    # pIndex= where do i put my pivot
    for i in range(start,end):
        if arr[i]<piviot:
            arr[i],arr[pIndex]=arr[pIndex],arr[i]
            pIndex+=1
    arr[pIndex],arr[end]=arr[end],arr[pIndex]
    return pIndex

def quick_sort(arr,start,end):
    if start<end:
        pIndex=partition(arr,start,end)
        # left recursion
        quick_sort(arr,start,pIndex-1)
        # right
        quick_sort(arr,pIndex+1,end)
    return arr

def sort(arr):
    return quick_sort(arr,0,len(arr)-1) 

print(sort([33,4,22,1,0,-1,9]))
def partition(arr,start,end): 
    pivot = arr[end]     # pivot 
    pIndex=start
    for i in range(start,end): 
        if  arr[i] <= pivot: 
            # increment index of smaller element 
            arr[i],arr[pIndex] = arr[pIndex],arr[i] 
            pIndex+=1
    arr[pIndex],arr[end]=arr[end],arr[pIndex]
    return pIndex
def quickSort(arr,start,end): 
    if start < end: 
        pIndex = partition(arr,start,end) 
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, start, pIndex-1) 
        quickSort(arr, pIndex+1, end)
    return arr
def sort(arr):
    return (quickSort(arr,0,len(arr)-1))

print(sort([38,27,43,3,9,82,10]))

print(sort([5,2,3,1]))
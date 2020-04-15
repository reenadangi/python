def mergeSort(arr):
    # 1. Find mid
    # 2. left merge sort/right merge sort
    # 3. Merge left and right in arr
    if len(arr)>1:
        # find a mid point
        mid=len(arr)//2
        # left
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        # right
        mergeSort(right)
        
        # compare and merge
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr
    
print(mergeSort([-1,3,0,5,6,22,5,1,33,9]))
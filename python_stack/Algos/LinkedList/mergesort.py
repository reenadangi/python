def mergeSort(arr):
    # find mid
    if len(arr)>1:
        # find middle
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)
        
        i=j=k=0
        while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    arr[k]=left[i]
                    i+=1
                    k+=1
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
    else:
        return arr

print(mergeSort([3,5,6,22,3,1,0,-1]))
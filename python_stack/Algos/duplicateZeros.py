def duplicateZeros(arr):
    n=len(arr)
    i=0
    while i<n-1:
        if arr[i]==0:
            arr.insert(i+1,0)
            i+=1
        i+=1
    del arr[n:]
    return arr
print(duplicateZeros([1,0,2,3,0,4,5,0]))
        
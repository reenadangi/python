def removeDuplicates(arr):
    arr=sorted(arr)
    i=0 
    for j in range(i+1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return arr[:i+1]
    
print(removeDuplicates([1,2,3,4,5,6,3,4,7]))
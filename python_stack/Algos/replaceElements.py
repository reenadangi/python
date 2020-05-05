def replaceElements(arr):
    for i in range(len(arr)-1):
        arr[i]=max(arr[i+1:])
        print(arr[i])
    arr[-1]=-1    
    return arr
print(replaceElements([17,18,5,4,6,1]))
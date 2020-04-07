def countElements(arr):
    arr=sorted(arr)
    print(arr)
    count=0
    for i in range (len(arr)):
        if arr[i]+1 in arr:
            count+=1
    return count
print(countElements([1,2,3]))
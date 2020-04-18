def containsDuplicates(arr):
    arr=sorted(arr)
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            return True
    return False
print(containsDuplicates([3,4,5,2,1,23]))

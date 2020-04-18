def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                # swap
                arr[i],arr[j]=arr[j],arr[i]
    return arr
print(sort([44,55,3,6,2,-1,0,-1]))

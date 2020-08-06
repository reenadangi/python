def minMaxAvg(arr):
    max=arr[0]
    min=arr[0]
    total=0
   
    for i in range(len(arr)):
        if(max<arr[i]):
            max=arr[i]
        if(min>arr[i]):
            min=arr[i]
        total+=arr[i]
    return f"min:{min} max:{max} avg:{total/len(arr)}"


print(minMaxAvg([1,2,3,5,8]))
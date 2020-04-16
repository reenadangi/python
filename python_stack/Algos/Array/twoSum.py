def twoSum(arr,target):
    result = 0
    for i in range(len(arr)):
        result = target - arr[i]
        # check if reminder is there in rest of the array
        if result in arr[i+1:]:
            return [i, arr.index(result, i+1, len(arr))]  
            

print(twoSum([2,7,11,15],9))
       
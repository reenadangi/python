def reverseArray(arr):
    # inplace
    start=0
    end=len(arr)-1
    while start<end:
        # swap
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
print(reverseArray([4,5,6,7,8,9]))


    

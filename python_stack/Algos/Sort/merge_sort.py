def merge_sort(arr):
    if len(arr)>1:
        # find mid
        mid=len(arr)//2
        left=merge_sort(arr[:mid])
        right=merge_sort(arr[mid:])
        #check and merge left and rigth into arr
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
                k+=1
            else:
                arr[k]=left[j]
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

print(merge_sort([1,3,0,-1,7,4]))


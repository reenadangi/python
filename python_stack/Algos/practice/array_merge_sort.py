# merge sort
# divide and conquer
# find the mid point and keep going down and then merge
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        # merge_sort left and right
        
        left=merge_sort(arr[:mid])
        right=merge_sort(arr[mid:])

        # compare and merge
        i=j=k=0  
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
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
print(merge_sort([2,77,3,88,9,2,19,-1]))        
            


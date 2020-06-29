def reverseArray(arr,start,end):
    if len(arr)>1:
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    return arr
    
def rotateArray(nums,k):
    n=len(nums)-1
    k=k%n
    nums=reverseArray(nums,0,n) 
    # 7,6,5,4,3,2,1
    nums=reverseArray(nums,0,k-1)
    nums=reverseArray(nums,k,n)
    return nums
    
print(rotateArray([1,2,3,4,5,6,7],3))
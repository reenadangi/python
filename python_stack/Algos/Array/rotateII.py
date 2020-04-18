def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
def rotate(arr,k):
    n=len(arr)
    k=k%n
    arr=reverse(arr,0,len(arr)-1)
    arr=reverse(arr,0,k-1)
    arr=reverse(arr,k,n-1)
    print (arr)
rotate([1,2,3,4,5,6,7,8],2)
# 7 8 1 2 3 4 5 6 7
# 8 7 6 5 4 3 2 1
# 7 8 6 5 4 3 2 1


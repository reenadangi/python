def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
def rotate(arr,k):
    n=len(arr)-1
    # no of times optimization
    k=k%n 
    arr=reverse(arr,0,n)
    arr=reverse(arr,0,k-1)
    arr=reverse(arr,k+1,n)
    return arr
print(rotate([1,2,3,4,5,8,7,6],3))
# 6 1..
# 7 6 1...
# 8 7 6 1...
# reverse
# 6 7 8 5 4 3 2 1 
# 8 7 6 5 4 ..
# 8 7 6 1 2 3 4



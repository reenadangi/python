arr=[5,2,3,1]
def bubble_sort(arr):
    count=0
    for i in range(len(arr)):
        count=count+1
        for j in range(i+1,len(arr),1):
            count=count+1
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    print(count)
bubble_sort(arr)
print(arr)
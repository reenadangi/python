arr=[1,3,6,7,9,2]
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr),1):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
       
bubble_sort(arr)
print(arr)
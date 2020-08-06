def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                print(f"swap {arr[i]} {arr[j]},")
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)
bubbleSort([3,14,-5,6,7,0])        
    
def containts(arr,num):
    if num in arr:
        return arr.index(num,0,len(arr)-1)

    
print(containts([1,33,3,33,5,6,7,33,9,10],33))
def remove(arr,n):
    # find the element
    # remove 
    # shift other elements
    # arr2=[] 
    # for i in arr:
    #     if i!=n:
    #         arr2.append(i)
    # return arr2
    arr.remove(n)
    return arr           

def removeLast(arr,n):
   index=arr[::-1].index(n)
   del arr[(len(arr)-1-index)]
   return arr


print(remove([2,3,0,4,5,6,7,8,9,0],0))
print(removeLast([2,3,0,4,5,6,7,8,9,0,19],0))
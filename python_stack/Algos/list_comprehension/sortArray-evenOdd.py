def sort(arr):
    even=[n for n in arr if n%2==0]
    odd=[n for n in arr if n%2!=0]
    return even+odd
print(sort([1,2,3,4,5,6,7,8,9,10]))
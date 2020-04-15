# find how many number contains even no of digits
def findNumbers(nums):
    even=0
    for i in nums:
        if len(str(i))%2==0:
            even+=1
    return even
print(findNumbers([12,345,2,6,7896]))
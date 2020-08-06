def repeteTwice(nums):
    arr=[]
    for i in nums:
        arr.append(i)
        arr.append(i)
    return arr
print(repeteTwice([4,"Ulysses", 42]))

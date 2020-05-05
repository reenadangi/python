def kidsWithCandies(candies, extraCandies):
    arr=[]
    for i in range(len(candies)):
        if candies[i]+ extraCandies>max(candies):
            arr.append(True)
        else:
            arr.append(False)
    return arr

print(kidsWithCandies([12,1,12],10))


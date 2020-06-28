def minMaxAvg(lst):
    print(lst[0])
    min=lst[0]
    max=lst[0]
    sum=lst[0]
    
    for i in lst:
        if i>max:
            max=i
        if i<min:
            min=i
        sum+=i
    print(f"min: {min} max: {max} avg:{sum/len(lst)}")
minMaxAvg([12,3,4,5,10,18,78])
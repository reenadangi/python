def minMaxAvg(my_lst):
    min=my_lst[0]
    max=my_lst[0]
    total=0
    for i in my_lst:
        if min>i:
            min=i
        if max<i:
            max=i
        total+=i
    avg=total/len(my_lst)
    print(f"Min {min}, Max {max}, Avg {avg}")
minMaxAvg([2,3,4,5,6,7,1])
        
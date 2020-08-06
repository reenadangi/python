# Selection sort - find the min and swap with front
# def find_min(lst):
#     min=lst[0]
#     for i in range(len(lst)):
#         if lst[i]<min:
#             min=lst[i]
#     return min

lst=[7,14,5,16,2]
for i in range(len(lst)):
    min=lst[i]
    min_at=i
    for j in range(i+1,len(lst),1):
        print("looking for min")
        if lst[j]<min:
            # min_at
            min=lst[j]
            min_at=j
            print(f"Minimum is :{min}at {min_at}")
        # if we need to swap
    if min_at!=i:
        print(f"lets swap {lst[i]},{lst[min_at]}","*"*24)
        lst[i],lst[min_at]=lst[min_at],lst[i]
    print(lst)


print (lst)


    

print(min)

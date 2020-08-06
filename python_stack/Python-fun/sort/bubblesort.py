lst=[1,9,3,4,5,6,2]
for i in range(0,len(lst),1):
    for j in range(i+1,len(lst),1):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
    
print(lst)


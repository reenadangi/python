def bubblesort(l,n):
    for i in range(len(l)-2):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    if n>1:        
        bubblesort(l,n-1)   

l = [6,2,9,11,9,3,7,12]
n=len(l)    
bubblesort(l,n)
print(l)


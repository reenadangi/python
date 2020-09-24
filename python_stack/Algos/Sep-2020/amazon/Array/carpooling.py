def carPooling( trips, capacity):
    lst=[]
    for ppl, start, end in trips:
        lst.append((start,ppl))
        lst.append((end,-ppl))
    
    lst.sort()
    
    for _ ,ppl in lst:
        capacity -= ppl
        if capacity<0:
            return False
    return True
print(carPooling([[2,1,5],[3,3,7]],4))
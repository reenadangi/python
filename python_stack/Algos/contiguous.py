#[0,1,1,0,1,1,0,1] 
# -1 0 1 0 1 2 1 0 
def contiguousSubArray(nums):
    max_len=0
    counts={}
    count=0
    for i in range(len(nums)):
        # if 0 decrement the counter
        # if 1 increment the counter
        if nums[i]==0:
            count+=-1
        else:
            count+=1
        counts.append(count,i)
    
            
    
    return max(count)

    
print(contiguousArray([0,1]))

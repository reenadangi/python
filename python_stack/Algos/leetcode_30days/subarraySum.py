def subarraySum(nums,k):
    sum=0
    count=0
    my_dict={}
    for i in range(len(nums)):
        sum+=nums[i]
        if sum==k:
            count+=1
        if(sum-k in my_dict):
            count+=my_dict[sum-k]
        if(sum in my_dict):
            my_dict[sum]+=1
        else:
            my_dict[sum]=1
        i+=1
    return count
def another(nums,k):
    count=0
    sum=0
    for i in nums:
        sum+=i
        if sum==k:
            count+=1
            sum=0
        
    return count




print(another([1,1,1],3))
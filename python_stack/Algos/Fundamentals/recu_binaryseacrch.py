def searchRec(nums,value,start,end):
    if start<=end:
        mid=(start+end)//2
        if value==nums[mid]:
            return True
        elif value>nums[mid]:
            return searchRec(nums,value,mid+1,end)
        else:
            return searchRec(nums,value,start,mid-1)
    else:
        return False

def search(nums,value):
    return searchRec(nums,value,0,len(nums)-1)

print(search([2,3,4,5,6,7,8],14))
       


def isbadVersion(n):
    if n==6:
        return True
    else:
        return False 

def firstBadVersion(n):
    left=1
    right=n
    bad=right
    while(left<=right):
        mid=(left+right)/2
        if isbadVersion(mid):
            bad=mid
            right=mid-1
        else:
            left=mid+1
        return bad
print(f"First Bad Version is {firstBadVersion(20)}")
            
        
        
# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
def canReach(arr, start):
        s=[]
        s.append(start)
        seen=[]
        while s:
            m=s.pop()
            l=m-arr[m]
            r=m+arr[m]
            if l>=0 and l<len(arr) and l not in seen:
                s.append(l)
                seen.append(l)
                if arr[l]==0:
                    return True
            if r>=0 and r<len(arr) and r not in seen:
                s.append(r)
                seen.append(r)
                if arr[r]==0:
                    return True
                
        return False
print(canReach([4,2,3,0,3,1,2],3))


def max_sub(nums):
    # Store infinate 
   inf=float('inf')
   best=-inf
   sumSoFar=0
   for i in nums:
       sumSoFar+=i
       best=max(sumSoFar,best)
       sumSoFar=max(sumSoFar,0)
   return best

print(max_sub([-2,1,2,-2,-1]))
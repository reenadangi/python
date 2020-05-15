# def maxSubarraySumCircular(A):
#     #Use dynamic programming - Kadaneis Algo
#     max_sum=current_sum=A[0]
#     for i in range(1,len(A)):
#         current_sum=max(A[i]+current_sum,A[i])
#         max_sum=max(current_sum,max_sum)
#     return max_sum

# def maxSubarraySumCircular( A):
#         total_1=A[:]
#         total_2=A[:]
#         cir_sum=0
#         for i in range(1,len(A)):
#             if  total_1[i-1]>0:
#                 total_1[i]+= total_1[i-1]
#                 cir_sum=1
#             if  total_2[i-1]<0:
#                 total_2[i]+= total_2[i-1]
#         if cir_sum==0:
#             return max(A)
#         return max(max(total_1),(sum(A)-min(total_2)))

def maxSubarraySumCircular(A):
    if len(A) == 0:
            return 0
    maxTotal,maxSoFar,minSoFar,minTotal,s = A[0], A[0], A[0], A[0],A[0]
    for i in range(1, len(A)):
        maxSoFar = max(A[i], maxSoFar + A[i])
        maxTotal = max(maxTotal, maxSoFar)            
            
        minSoFar = min(A[i], minSoFar + A[i])            
        minTotal = min(minTotal, minSoFar)            
        s += A[i]
    if(s == minSoFar):
        return maxTotal
        
    return max(s - minTotal, maxTotal)

print(maxSubarraySumCircular([3,-1,2,-1]))

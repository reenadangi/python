import heapq
def minCost(arr):
    heapq.heapify(arr) 
    sum = 0
    while(len(arr) > 1): 
        first = heapq.heappop(arr) 
        second = heapq.heappop(arr) 
        sum += first + second 
        heapq.heappush(arr, first + second) 
    return sum 


print(minCost([1,2,3,4,5]))
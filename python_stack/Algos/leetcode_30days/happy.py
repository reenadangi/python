# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
def numSquareSum(n): 
    sum = 0; 
    while(n): 
        sum += (n % 10) * (n % 10); 
        n = int(n / 10); 
    return sum; 
def isHappy(n):
    slow=n
    fast=n
    while(True):
        slow=numSquareSum(slow)
        fast=numSquareSum(numSquareSum(fast))
        if slow==fast:
            break
    return slow==1

print(isHappy(19))

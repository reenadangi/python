# Given an integer, write a function to determine if it is a power of two.
def isPowerOfTwo(n):
    if n<=0: return False
    while n%2==0:
        n=n/2
    return n==1
print(isPowerOfTwo(5))

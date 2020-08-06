def fact(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact
def factorial(n):
    # recursive 
    if n==0:
        return 1
    return n*factorial(n-1) 

print(fact(6))
print(factorial(6))

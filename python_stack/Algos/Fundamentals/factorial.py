def factorial(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    print(fact)
factorial(4)
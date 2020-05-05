def subtractProductAndSum(n):
    sum=0
    prod=1
    while(n):
        sum+=n%10
        prod=prod*(n%10)
        n=n//10
    print(sum,prod)
subtractProductAndSum(234)
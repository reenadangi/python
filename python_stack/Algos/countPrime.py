def countPrimes( n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)
print(countPrimes(12))

def countPrime2(num):
    # set all are Prime
    primes = [1] * num
    primes[0]=primes[1]=0
    # for i in range(2,num):
    for i in range(2,int(num**0.5)+1):
        if primes[i]==1:
            j=2
            while(i*j<num):
                primes[i*j]=0
                j+=1
    count=0
    for i in primes:
        if i==1:
            count+=1 
    return count
print(countPrime2(12))

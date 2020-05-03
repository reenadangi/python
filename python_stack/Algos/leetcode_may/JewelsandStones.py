def numJewelsInStones(J,S):
    return len([s for s in S if s in J ])
print (numJewelsInStones("aA","aAAbbbb"))

def sumToOne(num):
    strNum=str(num)
    if len(strNum)==1:
        return num
    sum=0
    while(len(strNum)>1):
        sum=0
        for c in strNum:
            sum+=int(c)
        strNum=str(sum)
    return sum
print(sumToOne(35))

def clockHandAngles(seconds): 
    hrs=seconds/60/60
    temp=seconds-(int(hrs) *60*60)
    min=temp/60
    temp1=int(min)*60
    secs=temp-temp1
    hDgree=round(hrs*30)
    mDgree=round((min*30)/5)
    sDgree=round((secs*30)/5)
    print(hDgree,mDgree,sDgree)

clockHandAngles(50000)

def  isPrime(num):
    for i in range(2,num-1):
        if num%i==0:
            return False
    return True
print(isPrime(4))
    

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
    
def heights(arr):
    res=[]
    for i in arr:
        if i>0 and i not in res:
            if len(res)>0:
                if i>res[-1]:
                    res.append(i)
            else:
                res.append(i)
    return res
print(heights([-1, 1, 1, 7, 3, 5, 9, -3, 3, 15] ))

def secondToLast(arr):
    if len(arr)>2:
        return arr[-2]
    else:
        return None
print(secondToLast([1]))
def nToLast(arr, n):
    if len(arr)>=n:
        return arr[-n]
    else:
        return None
print(nToLast(  [1,2,3,5,5,7,10], 1))
def removeRange(arr,i,j):
    arr=arr[:i]+arr[j+1:]
    print(arr)
removeRange([1,2,3,5,5,7,10],2,4)
def zipIt(arr1,arr2):
    i=0
    j=0
    arr3=[]
    while(i<len(arr1) or j<len(arr2)):
        if i<len(arr1):
            arr3.append(arr1[i])
            i+=1
        if j<len(arr2):
            arr3.append(arr2[j])
            j+=1   
    return arr3
print("zip",zipIt([1,2,34,5],[5,6]))

def multiTable(x,y):
    for i in range(1,y+1):
        for j in range(1,x+1):
            print (i*j)
multiTable(3,3)

def twoDimensional(row, column):
    arr=[]
    for i in range(row):
        temp=[]
        for j in range(column):
            temp.append(0)
        arr.append(temp)
    return arr    

print(twoDimensional(2,5))
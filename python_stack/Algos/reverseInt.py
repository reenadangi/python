# 1234
# 4321
def reverse_int(num):
    sum=0
    if num<0:
        num=num*-1
    while abs(num):
        r=num%10
        sum=sum*10+r
        num=int(num/10)
    if sum > (2 ** 31 - 1):
        return 0
    
    return sum
        
   
print(reverse_int(-124))

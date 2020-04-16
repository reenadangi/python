def plusOne(digits):
    carry=0
    for i in range(len(digits)-1,-1,-1):
        if carry:
                pass
        elif digits[i]+1>10:
           digits[i]=0
           carry=1
        elif carry==1:
            digits[i]+1


    
print(plusOne([4,3,2,1]))
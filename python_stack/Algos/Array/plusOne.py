def plusOne(digits):
    carry=0
    for i in range(len(digits)-1,-1,-1):
        digits[i]+=1
        # find if there is any carry
        carry=digits[i]//10
        # keep only last digit
        digits[i]=digits[i]%10
        if not carry:
            return digits
    if carry:
        return [1]+digits
print(plusOne([9,9,9]))
    
print(plusOne([4,3,2,1]))
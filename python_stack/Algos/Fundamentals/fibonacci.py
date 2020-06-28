# 0,1,1,2,3
def fibonacci(num):
    if num<0:
        return False
    elif num==0 or num==1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

    
print(fibonacci(4))
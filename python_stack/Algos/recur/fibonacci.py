# he Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# print nth fibonacci number
def fibonacci(n):
    if n<0:
        return False
    elif n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

    
print(fibonacci(4))

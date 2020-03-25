def fizzBuzz(number):
    result=""
    if number>0:
        for num in range(1,number+1):
            r=""
            if num%5==0 and num%3==0:
                r="FizzBuzz"
            elif num%5==0:
                 r="Fizz"
            elif num%3==0:
                 r="Buzz"
            else:
               r=f"{num}"
    else:
        result="Enter Valid Number"
    return result

print(fizzBuzz(15))
# Create a function called fizzbuzz that accepts a parameter n. Have the function log all the numbers from 1 to n in order with the following exceptions:

# If the number is divisible by both 3 and 5, log "FizzBuzz" instead of the number
# If the number is divisible by 3 but not by 5, log "Fizz" instead of the number
# If the number is divisible by 5 but not by 3, log "Buzz" instead of the number
def fizzbuzz(num):
    if num>0:
        result=""
        for n in range(1,num+1):
            
            if n%3==0 and n%5==0:
                r="FizzBuzz"
            elif n%3==0:
                r="Fizz"
            elif n%5==0:
                r="Buzz"
            else:
                r=f"{n}"
            result+=f"{r}, "

        return result
    else:
        return "Enter a valid number"
print(fizzbuzz(15))

def fizzBuzz(number):
    if number%5==0 and number%3==0:
        print("FIZZBUZZ")
    elif number%5==0:
        print("FIZZ")
    elif number%3==0:
        print("BUZZ")
    else:
        print("None")

fizzBuzz(10)
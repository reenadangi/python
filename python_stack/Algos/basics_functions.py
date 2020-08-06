#  Example: countdown(5) should return [5, 4, 3, 2, 1, 0]
def countdown(num):
    for i in range(num,0,-1):
        print(i)

# Example: print_and_return([1, 2]) should print 1 and return 2
def print_and_return(array):
    print(array[0])
    return array[1]

def sum(a,b):
    return a+b

# countdown(5)
# print(print_and_return([1,2]))
print(sum(9,10))

countdown(5)
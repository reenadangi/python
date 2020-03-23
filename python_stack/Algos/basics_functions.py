#  Example: countdown(5) should return [5, 4, 3, 2, 1, 0]
def countdown(num):
    array=[]
    for i in range(num,-1,-1):
        array.append(i)
    print(array)
# Example: print_and_return([1, 2]) should print 1 and return 2
def print_and_return(array):
    print(array[0])
    return array[1]

def sum(a,b):
    return a+b

# countdown(5)
# print(print_and_return([1,2]))
print(sum(9,10))

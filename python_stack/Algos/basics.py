def basic():
    for i in range(151):
        print (i)

def multiples_five():
    for i in range(5,1001,5):
        print (i)

# Counting, the Dojo Way - Print integers 1 to 100.
#  If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".
def the_dojo_way():
    for i in range(50):
        if i%10==0:
            print(i, "Coding Dojo")
        elif i%5==0:
            print(i,"Coding")

# Add odd integers from 0 to 1000 and print the final sum.
def add_odd():
    sum=0
    for i in range(0,1000):
        if i%2!=0:
            sum+=i 
    print ("Odd sum is",sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def print_positive():
    for i in range(2018,0,-4):
        print (i)


# basic()
# multiples_five()
# the_dojo_way()
# add_odd()
print_positive()


for i in range(-25000,30001,+1):
    if i%2!=0:
        sum+=i
return i
    
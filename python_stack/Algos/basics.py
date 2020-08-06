def basic():
    for i in range(151):
        print (i)

def multiples_five():
    for i in range(5,100,5):
        print(5)

# Counting, the Dojo Way - Print integers 1 to 100.
#  If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".
def the_dojo_way():
    for i in range(1,50):
        if i%10==0:
            print("Coding Dojo")
        elif i%5==0:
            print("Coding")
        else:
            print(i)

def add_odd():
    sum=0
    for i in range(1,10):
        if i%2!=0:
            sum+=i
    print(f"odd sum{sum}")
add_odd()
for i in range(-25000,1,+1):
    print(i)


the_dojo_way()
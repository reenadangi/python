# Create function ThreesFives() that adds each value from 100 and 4000000 (inclusive) if that value
# is evenly divisible by 3 or 5 but not both .
def ThreesFives():
    sum=0
    for i in range(1,10):
        if i%3==0 or i%5==0:
            if not (i%3==0 and i%5==0):
                sum+=i
    print(sum)
ThreesFives()

            



import random
def randInt(min=0,max=100 ):
    if min==0 and max==100:
        # random.random() returns a random floating number between 
        # 0.000 and 1.000 and thats why if we multiply resukt with max it will remain in range 
        return random.random() *max
    elif min==0:
        return random.random()* max
    elif min>0:
        # should print a random integer between 50 to 100
        return (random.random()* (max-min) + min)
    

print(randInt())
print(randInt(max=50))
print(randInt(min=80))
print(randInt(min=50, max=500))




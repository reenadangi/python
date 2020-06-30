import random
def randInt(max,min):
    num= round(random.random()*max + min)
    return num
print(randInt(100,10))

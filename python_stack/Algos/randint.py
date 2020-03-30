import random
def randint(min=0,max=100):
    possible_range=max-min
    return round(random.random() * possible_range + min)
    
print(randint(10,100))
print(randint(90))
print(randint(max=10))
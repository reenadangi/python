import numpy as np
x=np.arange(2,11)
print(f"odds {x[x%2!=0]}")

# find common,
y=np.arange(5,20)
print(y)
print(np.intersect1d(x,y))
print(np.setdiff1d(x,y))
print(np.union1d(x,y))

import numpy as np
x=np.zeros((3,4))
y=np.ones((4,2))
# any number array(shape and value)
z=np.full((3,4),7.8)
print(x,y,z,z.dtype)
# eye - Diagnal matrix
w=np.eye(4)
print(w)
y=np.diag([10,20,30,50])
print(y)

# arange(start,stop,intervel)
x=np.arange(1,10)
# 1-9
print(x)
x=np.arange(4,10)
print(x)
x=np.arange(0,100,10)
# 10 20 30 40 50 60 70 80 90
print(x)

# linspace(start,stop,end)
x=np.linspace(0,10,100)
print(x)

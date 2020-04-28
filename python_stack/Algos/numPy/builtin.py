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

import numpy as np
x=np.array([12,34,56,78,99])
y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Orginal array{x}")
# access
print(x[0],x[len(x)-1],x[-1],x[-2])
# Modify
for i in range(len(x)):
    x[i]=x[i]*2
# delete first and last element
x=np.delete(x,[0,4])
print(x)
print(y)
# delete first row (x axis) 
y=np.delete(y,[0],axis=0)
print(y)
# delete first col(y axis)
y=np.delete(y,[0],axis=1)
print(y)
# append
print(x.dtype)
x=np.append(x,[14.5,243])
print(x)
print(x.dtype)
# insert
x=np.insert(x,1,58)
print(x)
x=np.insert(x,2,3)
print(x)
y=np.insert(y,1,34,axis=1)
print(y)
# stacking - vstack/hstack
# It's important that size of stacks are same
x=np.array([1,2,3])
y=np.array([30,40,50])
z=np.vstack((x,y))
print(z)
# hstack - Horizontal
z=np.hstack((x,y))
print(z)


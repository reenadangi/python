import numpy as np
x=np.array([10,20,30,40,50,60])
y=np.array([[1,2,3],[4,5,6],[7,8,8]])

print(x[1:4])
# print(y[rows,cols])
# middle all row's middle col
# starting index is included and ending index in excluded 
print(y[0:,1:2])
print(y[0:,:1])
# all the elements in 3rd row
print(y[2:,])

# unique
z=np.unique(y)
print(z)
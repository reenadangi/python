import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[11,12,130],[13,14,15]])
c=np.array(["a","b","c"])
print(b)
print(b.ndim)
print(a.shape)
print(c.shape)

# 2 rows and cols
print(f"Shape of b{b.shape}")
print(f"Shape of c{c.shape}")
print(f"Type {b.dtype}")
print(f"Type {a.dtype}")
print(f"Type {c.dtype}")

# row,col
# first row
print(f"first row {b[0]}")
# last col
print(b[-1])
# 3nd col
print(f"2nd col {b[:,2]}")
# first col
print(f"1st col {b[:,0]}")

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
sarr=np.array(["Reena","Dojo","Miko"])
isArr=np.array([1,2,"reena"])
print(type(arr),type(sarr))
print(arr.dtype)
print(sarr.dtype)
print(arr.size,sarr.size)
print(arr.shape,sarr.shape)
print(type(isArr))
print(sarr.dtype)
f=np.array([1,2,3,4.5])
print(type(f))
print(f.dtype)
# specifing datatype - this will save values in int 
f=np.array([1,2,3,4.5],dtype=np.int64)
print(f)
np.save("my_np",f)
y=np.load("my_np.npy")
print(y)


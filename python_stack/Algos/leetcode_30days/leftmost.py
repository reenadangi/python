# (This problem is an interactive problem.)

# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

# BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.

arr=dim()
rows=arr[0]
cols=arr[1]
for row in rows:
    start=0
    end=cols
    while start<=end:
        mid=(start+end)/2
        if mat(mid,col)==1:


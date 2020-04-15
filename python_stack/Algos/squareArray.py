def squareArray(A):
    for i in range(len(A)):
        A[i]=A[i]*A[i]
    return sorted(A)
print(squareArray([-7,-3,2,3,11]))

        
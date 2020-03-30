# Generate a String With Characters That Have Odd Counts
def generateTheString(n):
    if n%2!=0: 
       return 'a'*n 
    else:
        print(n-1)
        return 'a'*(n-1)+'b'
print(generateTheString(20))
h="h"
n="ll"
def strStr(h,n):
    print(len(h)-len(n)+1)
    for i in range(len(h) - len(n) + 1):
            
            if h[i:i+len(n)] == n:
                return i
            return -1

print(strStr(h,n))



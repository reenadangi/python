def strStr(h,n):
    for i in range(len(h)-len(n)+1):
        if h[i:i+len(n)]==n:
            return i
        return -1
print(strStr("hello","ll"))
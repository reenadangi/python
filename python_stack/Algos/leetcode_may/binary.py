def toBin(num):
    i=1
    while i<=num:
        num^=i
        i<<=1
    print(num)
toBin(5)
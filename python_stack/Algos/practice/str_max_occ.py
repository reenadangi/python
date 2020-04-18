from collections import Counter
def max_occ(input):
   wc = Counter(input)
   # Finding maximum occurrence
   s = max(wc.values())
   i = wc.values().index(s)
   print (wc.items()[i])
  
           
print(max_occ("hello"))
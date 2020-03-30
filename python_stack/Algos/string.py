str="Hello There"
print(str[0])
print(str[-1])
# String slice
print(str[3:len(str)])

str='Dojo'
allUpper=True

print(str[0:])
if str[0].isupper() and str[1:].islower:
    print("true")
if str.isupper():
    print("true")
if str.lower():
    print ("true")

for c in str:
    if not c.isupper():
        allUpper=False
        break
print (f"This is Upper {allUpper}")
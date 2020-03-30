a=1233444545*800
print(type(a))
a=123.45
print(type(a))
a="hello world"
print(type(a))
a=2+3j
print(type(a))
print(a)
a='a'
print(type(a))
print('''this string has single (') and double (") quote.''')
a=True
print(type(a))
#Comosite types 
# Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
a=("dog",1,"cat",6)
print(type(a))
print(a[0])
print(a)
# List - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
a=["dog",1,"cat"]
a[0]="Camel" 
print(a)
# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods
a={
    "firstname":"Reena",
    "lastname":"dangi"
}
print(a["firstname"])
for key in a:
    print(f"{key} is {a[key]}")





x=[[5,2,3],[10,8,9]]
x[1][0]=15
print(x)

shark_tank=[
    {'firstname':'reena','last_name':'dangi'},
    {'firstname':'Mark','last_name':'Cubon'},
    {'firstname':'Lorie','last_name':'Greiner'}

]
for shark in shark_tank:
    print(shark['firstname'])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

for key in dojo.keys():
    print(key)
    for value in dojo[key]:
        print(value)
for key,value in dojo.items():
    print(key,value)
 
dojo_users = {
1: ["Samuel", 21, "Data Structures"],
2: ["Richie", 20, "Machine Learning"],
3: ["Lauren", 21, "OOPS with java"],
}
for key in dojo_users.keys():
    for value in dojo_users[key]:
        print(value)
for key,value in dojo_users.items():
    name,age,subject=value
    print(name,age,subject)

   
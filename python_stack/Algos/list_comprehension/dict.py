users=[
    {'name':'Tom','country':'USA','language':'python'},
    {'name':'Jhon','country':'usa','language':'java'},
    {'name':'Hollu','country':'England','language':'python'}
]
users=[user['name'] for user in users if user['country'].upper()=='USA']
print(users)


list1 = [1, 2, 3, 4, 1, 2, 6]  
list1.reverse()
print(list1)

 
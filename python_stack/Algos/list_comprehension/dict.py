users=[
    {'name':'Tom','country':'USA','language':'python'},
    {'name':'Jhon','country':'usa','language':'java'},
    {'name':'Hollu','country':'England','language':'python'}
]
users=[user['name'] for user in users if user['country'].upper()=='USA']
print(users)

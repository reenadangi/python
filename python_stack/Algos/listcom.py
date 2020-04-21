lst=[
    {'name':'Mike','city':'Chicago','language':'Python'},
    {'name':'Devon','city':'Siattle','language':'c#'},
    {'name':'Wes','city':'NY','language':'java'},
    {'name':'Donald','city':'chicago','language':'java'}
]

print([ [instructor['name'],instructor['city']] for instructor in lst if instructor['city'].lower()=='chicago'])








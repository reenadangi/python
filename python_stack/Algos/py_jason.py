import json
userJSON='{"name":"Reena","city":"Chicago"}'
# loads will load jason into dict
user=json.loads(userJSON)
for key in user:
    print (f"{key} {user[key]}")
print(user)
car={"model":"ford","model":"mustang","year":1970}
print (car)

carJSON=json.dumps(car)
print(carJSON)
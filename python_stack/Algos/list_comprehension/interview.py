print([n for n in range(1,101)])
nums=[1,2,2,3,3,4,5,6,7]
print([n for n in nums if n%2==0])
cars=[
    {'brand':'Ford','model':'Mustang','year':1964},
    {'brand':'Ford','model':'Ranger','year':1960},
    {'brand':'Audi','model':'A8','year':2008},
    {'brand':'BMW','model':'X7','year':2007}
]
print([[car['brand'],car['model']] for car in cars if car['year']>=2000])
# remove duplicates 
res=[]
[res.append(i) for i in nums if i not in res ]
print(res)
# defangIPaddr - replace all . to [.]
ip='123.123.180.80'
res=''.join([c if c!='.' else '[.]' for c in ip])
print(res)

# j - stones that are jewels
# s - type of stones you have
#  Find out how many jwels you have
j='aA'
s='aAAbbbba'
print([stone for stone in s if stone in j])

brands=['Ford','Audi','BMW']
cars=['Ranger','A8','X7']

# result [Ford, Ranger] [Audi,A8] [BMW,X7]
# I want a dict 'brand':'car' for each brand and car
my_dict={}
for brand,car in zip(brands,cars):
    my_dict[brand]=car
print(my_dict)
my_dict={brand:car for brand,car in zip(brands,cars) if brand!="Ford"}
print(my_dict)
# this will create tuples which 

# set comprehension 
# set is like list - but it has all unique values 
nums=[1,2,3,4,5,6,1,3,4,9]
my_set=set()
# for n in nums:
#     my_set.add(n)
# print(my_set)
my_set={n for n in nums}
print(my_set)



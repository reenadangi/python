print([n for n in range(1,101)])
nums=[1,2,2,3,3,4,5,6,7]
print([n for n in nums if n%2==0])
cars=[
    {'model':'BMW','year':2000},
    {'model':'Audi','year':1995},
    {'model':'Merc','year':1999}
]
print([[car['model'],car['year']] for car in cars if car['year']>=2000])
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





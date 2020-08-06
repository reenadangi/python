#  LIST COMPREHENSIONS
# 1. return a list of numbers between (1-100)
# 2. List - I want n for each n in nums[1,2,3,4,5,6,7,8,9,10] -(even/odd)
# 3. NESTED FOR LOOPS I want (letter,num) pair for each letter in ('abcd') and each num in(0123)
# 4. List of dictionary- return list of brand and models for year>2000
# cars=[
#     {'brand':'Ford','model':'Mustang','year':1964},
#     {'brand':'Ford','model':'Ranger','year':1960},
#     {'brand':'Audi','model':'A8','year':2008},
#     {'brand':'BMW','model':'X7','year':2007}
#     ]
# 5. Creating a dictionary with list comprehensions 
# brands=['Ford','Audi','BMW']
# cars=['Ranger','A8','X7']
    # {'Ford':'Ranger','Audi':'A8','BMW','X7'}
    # I want a dict 'brand':'car' for each brand and car
# [expression iteration condition]
# 6. # set comprehension 
# set is like list - but it has all unique values 
# 7. Remove Duplicate 
# nums=[1,2,3,3,4,4,5,6,6,7,8]
# b=[]
# [b.append(n) for n in nums if n not in b]
# print(b)

nums=[1,2,3,3,4,4,5,6,6,7,8]
b=[]
[b.append(n) for n in nums if n not in b]
print(b)




    
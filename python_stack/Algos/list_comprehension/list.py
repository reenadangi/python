nums=[1,2,3,4,5,6]
my_list=[]
# for i in nums:
#     my_list.append(i)
# print (my_list)

# 1. First example
my_list=[i for i in nums]
print(my_list)
# 2. I want n*n for each in nums
my_list=[]
my_list=[i*i for i in nums]
print(my_list)
# 3. I want i for each in mums if i is even
my_list=[]
my_list=[i for i in nums if i%2==0]
print(my_list)
# 4. NESTED FOR LOOPS I want (letter,num) pair for each letter in ('abcd') and each num in(0123)
my_list=[]
# for letter in 'abcd':
#     for num in range(4):
#         # tuple of letter and num
#         my_list.append((letter,num))
# print(my_list)
my_list=[(letter,num)for letter in 'abcd' for num in range(4) ]
print(my_list)
# 5. Dict
my_list=[]
names=['Bruce','clark','Peter','Logan']
heros=['batman','superman','spiderman','wolverine']
# for name,hero in zip(names,heros):
#     my_list[name]=hero
# print (my_list)
# if name is not clark
my_list={name:hero for name,hero in zip(names,heros) if name!='clark'}
print(my_list)
# 6. Set compriherntion - all unique
nums=[1,2,3,3,3,1,4,5,6]
# my_set=set()
# for i in nums:
#     my_set.add(i)
# print(my_set) 
my_set={i for i in nums}
print(my_set)



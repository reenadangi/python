lst=[1,2,3,4]
lst2=[1,6,7,8]
lst3=[]
[lst3.append([x,y]) for x in lst for y in lst2 if x!=y ]
print(lst3)

# lst3=[]
# for x in lst:
#     for y in lst2:
#         if x!=y:
#             lst3.append([x,y])
# print (lst3)
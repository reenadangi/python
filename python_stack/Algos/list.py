# There are no arrays in python - List can be used as array
my_list=['Reena','Lee','Mark']
my_list.append('Dalayla')
my_list.reverse()
my_list.extend('Barbara')
my_list.sort()
my_list.insert(2,"New")
print(my_list[0])
print(my_list)
# last value can be accessed at -1
print(my_list[-1]) 
print(len(my_list))
# returns items before 2
print(my_list[:2])
# return item  2 and after
print(my_list[2:])
print(f"My list {my_list[::-1]}")

